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


