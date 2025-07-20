module "li10_network_switch" {
  source = "./modules/li10-network-switch"

  ecs_cluster_name   = aws_ecs_cluster.production.name
  ecs_service_name   = aws_ecs_service.production.name
  public_subnet_ids  = [aws_subnet.public-subnet-1.id, aws_subnet.public-subnet-2.id]
  private_subnet_ids = [aws_subnet.private-subnet-1.id, aws_subnet.private-subnet-2.id]
  security_group_ids = [aws_security_group.ecs-fargate.id]
}

resource "aws_lambda_invocation" "network_switch_invocation" {
  function_name = module.li10_network_switch.network_switch_lambda_name

  input = jsonencode({
    network_mode = var.network_mode
  })
}