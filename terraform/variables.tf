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

