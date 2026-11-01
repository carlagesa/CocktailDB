output "network_switch_lambda_name" {
  description = "The name of the network switch lambda function."
  value       = aws_lambda_function.network_switch_lambda.function_name
}