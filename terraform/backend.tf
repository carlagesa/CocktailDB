terraform {
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 5.82.2"
        }
    }
  backend "s3" {
    bucket         = "cocktail-tf-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    use_lockfile = true # Enables S3 native state locking
  }
}
