provider "aws" {
  region = var.region

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