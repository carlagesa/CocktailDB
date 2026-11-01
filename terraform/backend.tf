terraform {
  required_version = ">= 1.10.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.82.2"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6.0"
    }
  }

  # Temporarily using local backend for testing without AWS credentials.
  # The production configuration uses the S3 backend:
  #   backend "s3" {
  #     bucket       = "cocktail-tf-state"
  #     key          = "production/terraform.tfstate"
  #     region       = "us-east-1"
  #     use_lockfile = true
  #     encrypt      = true
  #   }
  backend "local" {
    path = "terraform.tfstate"
  }
}