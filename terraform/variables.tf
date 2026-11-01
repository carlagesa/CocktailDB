variable "region" {
  description = "The AWS region to create resources in."
  default     = "us-east-1"
}

variable "image_tag" {
  description = "Tag of the Docker image to deploy"
  type        = string
}

variable "rds_hostname" {
  description = "The hostname of the RDS instance"
  type        = string
}

variable "rds_db_name" {
  description = "RDS database name"
  default     = "mydb"
}

variable "rds_username" {
  description = "RDS master username"
  type        = string
}

variable "rds_instance_class" {
  description = "RDS instance type"
  default     = "db.t3.micro"
}

variable "network_mode" {
  description = "The network mode for the ECS service (public or private)."
  type        = string
  default     = "private"
}

variable "public_subnet_1_cidr" {
  description = "CIDR Block for Public Subnet 1"
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIDR Block for Public Subnet 2"
  default     = "10.0.2.0/24"
}

variable "private_subnet_1_cidr" {
  description = "CIDR Block for Private Subnet 1"
  default     = "10.0.3.0/24"
}

variable "private_subnet_2_cidr" {
  description = "CIDR Block for Private Subnet 2"
  default     = "10.0.4.0/24"
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1b", "us-east-1c"]
}

variable "health_check_path" {
  description = "Health check path for the default target group"
  default     = "/health_check"
}

variable "log_retention_in_days" {
  description = "Number of days to retain CloudWatch logs"
  type        = number
  default     = 30
}

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "production"
}

variable "docker_image_url_django" {
  description = "Docker image to run in the ECS cluster"
  default     = "626690050115.dkr.ecr.us-east-1.amazonaws.com/django-app:latest"
}

variable "docker_image_url_nginx" {
  description = "Docker image to run in the ECS cluster"
  default     = "626690050115.dkr.ecr.us-east-1.amazonaws.com/nginx:latest"
}

variable "app_count" {
  description = "Number of Docker containers to run"
  type        = number
  default     = 2
}

variable "autoscale_min" {
  description = "Minimum autoscale (number of tasks)"
  type        = number
  default     = 1
}

variable "autoscale_max" {
  description = "Maximum autoscale (number of tasks)"
  type        = number
  default     = 10
}

variable "autoscale_desired" {
  description = "Desired number of tasks to run initially"
  type        = number
  default     = 4
}