output "alb_hostname" {
  value = aws_lb.production.dns_name
}

output "ecs_task_execution_role_arn" {
    value = aws_iam_role.ecs-task-execution-role.arn
    description = "ARN for the ECS Task Execution Role"
}

output "subnets" {
  value = [aws_subnet.public-subnet-1.id, aws_subnet.public-subnet-2.id]
}

output "security_group" {
  value = aws_security_group.ecs-fargate.id
}
output "network_switch_lambda_name" {
  description = "The name of the network switch lambda function."
  value       = module.li10_network_switch.network_switch_lambda_name
}