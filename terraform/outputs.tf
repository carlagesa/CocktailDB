output "alb_hostname" {
  description = "DNS name of the application load balancer"
  value       = aws_lb.production.dns_name
}

output "ecs_task_execution_role_arn" {
  description = "ARN for the ECS Task Execution Role"
  value       = aws_iam_role.ecs-task-execution-role.arn
}

output "subnets" {
  description = "IDs of the public subnets"
  value       = [aws_subnet.public-subnet-1.id, aws_subnet.public-subnet-2.id]
}

output "security_group" {
  description = "ID of the ECS Fargate security group"
  value       = aws_security_group.ecs-fargate.id
}

output "network_switch_lambda_name" {
  description = "The name of the network switch lambda function."
  value       = module.li10_network_switch.network_switch_lambda_name
}