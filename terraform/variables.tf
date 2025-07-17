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

variable "rds_password" {
  description = "The RDS password"
  type        = string
  sensitive   = true
  default     = "Concorde@003" # Change this to a secure password or use a secret management solution
}
