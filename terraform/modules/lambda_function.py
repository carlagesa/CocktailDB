import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ecs = boto3.client("ecs")


def lambda_handler(event, context):
    cluster_name = os.environ["ECS_CLUSTER_NAME"]
    service_name = os.environ["ECS_SERVICE_NAME"]
    public_subnets = os.environ["PUBLIC_SUBNETS"].split(",")
    private_subnets = os.environ["PRIVATE_SUBNETS"].split(",")
    security_groups = os.environ["SECURITY_GROUPS"].split(",")

    network_mode = event.get("network_mode", "private").lower()

    logger.info(
        "Updating service %s in cluster %s to use %s subnets.",
        service_name,
        cluster_name,
        network_mode,
    )

    if network_mode == "public":
        subnets = public_subnets
        assign_public_ip = "ENABLED"
    else:
        subnets = private_subnets
        assign_public_ip = "DISABLED"

    try:
        ecs.update_service(
            cluster=cluster_name,
            service=service_name,
            networkConfiguration={
                "awsvpcConfiguration": {
                    "subnets": subnets,
                    "securityGroups": security_groups,
                    "assignPublicIp": assign_public_ip,
                }
            },
            forceNewDeployment=True,
        )
        logger.info("Service %s updated successfully.", service_name)
        return {
            "statusCode": 200,
            "body": json.dumps(
                f"Service {service_name} switched to {network_mode} network mode."
            ),
        }
    except Exception as exc:
        logger.error("Error updating service: %s", exc)
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error updating service: {exc}"),
        }
