variable "private_subnet_id" {
  description = "The ID of the private subnet."
  type        = string
}

variable "public_subnet_id" {
  description = "The ID of the public subnet."
  type        = string
}

variable "private_route_table_id" {
  description = "The ID of the private route table."
  type        = string
}

variable "ecs_cluster_arn" {
  description = "The ARN of the ECS cluster."
  type        = string
}