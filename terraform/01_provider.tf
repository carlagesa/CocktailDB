provider "aws" {
  region = var.region

  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_region_validation     = true
  skip_requesting_account_id = true

  default_tags {
    tags = {
      Project     = "cocktaildb"
      Environment = "production"
      ManagedBy   = "terraform"
    }
  }
}

provider "random" {
}