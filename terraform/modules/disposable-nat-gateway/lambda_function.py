import boto3
import os
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client('ec2')

def get_running_tasks_count(cluster_arn):
    ecs = boto3.client('ecs')
    running_tasks = ecs.list_tasks(cluster=cluster_arn, desiredStatus='RUNNING')
    return len(running_tasks['taskArns'])

def create_nat_gateway(public_subnet_id):
    logger.info("Creating NAT Gateway")
    try:
        eip_alloc = ec2.allocate_address(Domain='vpc')
        nat_gw = ec2.create_nat_gateway(
            SubnetId=public_subnet_id,
            AllocationId=eip_alloc['AllocationId']
        )
        nat_gateway_id = nat_gw['NatGateway']['NatGatewayId']
        waiter = ec2.get_waiter('nat_gateway_available')
        waiter.wait(NatGatewayIds=[nat_gateway_id])
        logger.info(f"NAT Gateway {nat_gateway_id} created.")
        return nat_gateway_id, eip_alloc['AllocationId']
    except Exception as e:
        logger.error(f"Error creating NAT Gateway: {e}")
        return None, None

def delete_nat_gateway(nat_gateway_id, allocation_id):
    logger.info(f"Deleting NAT Gateway {nat_gateway_id}")
    try:
        ec2.delete_nat_gateway(NatGatewayId=nat_gateway_id)
        waiter = ec2.get_waiter('nat_gateway_deleted')
        waiter.wait(NatGatewayIds=[nat_gateway_id])
        ec2.release_address(AllocationId=allocation_id)
        logger.info(f"NAT Gateway {nat_gateway_id} deleted.")
    except Exception as e:
        logger.error(f"Error deleting NAT Gateway: {e}")

def create_route_to_nat(route_table_id, nat_gateway_id):
    logger.info(f"Creating route to NAT Gateway {nat_gateway_id} in route table {route_table_id}")
    try:
        ec2.create_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock='0.0.0.0/0',
            NatGatewayId=nat_gateway_id
        )
    except Exception as e:
        logger.error(f"Error creating route: {e}")

def delete_route_to_nat(route_table_id):
    logger.info(f"Deleting route from route table {route_table_id}")
    try:
        ec2.delete_route(
            RouteTableId=route_table_id,
            DestinationCidrBlock='0.0.0.0/0'
        )
    except Exception as e:
        logger.error(f"Error deleting route: {e}")

def lambda_handler(event, context):
    cluster_arn = event['resources'][0]
    private_subnet_id = os.environ['PRIVATE_SUBNET_ID']
    public_subnet_id = os.environ['PUBLIC_SUBNET_ID']
    route_table_id = os.environ['ROUTE_TABLE_ID']

    running_tasks_count = get_running_tasks_count(cluster_arn)
    
    # Check for existing NAT Gateway
    response = ec2.describe_nat_gateways(
        Filters=[
            {'Name': 'subnet-id', 'Values': [public_subnet_id]},
            {'Name': 'state', 'Values': ['pending', 'available']}
        ]
    )
    nat_gateways = response.get('NatGateways', [])

    if running_tasks_count > 0 and not nat_gateways:
        logger.info("Tasks are running, but no NAT Gateway found. Creating one.")
        nat_gateway_id, allocation_id = create_nat_gateway(public_subnet_id)
        if nat_gateway_id:
            create_route_to_nat(route_table_id, nat_gateway_id)
    elif running_tasks_count == 0 and nat_gateways:
        logger.info("No running tasks, but NAT Gateway found. Deleting it.")
        for ngw in nat_gateways:
            delete_route_to_nat(route_table_id)
            delete_nat_gateway(ngw['NatGatewayId'], ngw.get('AllocationId'))
    else:
        logger.info("No action needed.")

    return {
        'statusCode': 200,
        'body': 'Function executed successfully!'
    }