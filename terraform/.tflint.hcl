# tflint configuration for CocktailDB Terraform
# Run: tflint --init && tflint --recursive

plugin "aws" {
  enabled  = true
  version  = "0.50.0"
  source   = "github.com/terraform-linters/tflint-ruleset-aws"
}

rule "terraform_required_providers" {
  enabled = true
}

rule "terraform_typed_interpolation" {
  enabled = true
}

rule "terraform_unused_declarations" {
  enabled = true
}

rule "terraform_naming_convention" {
  enabled = true
  naming_pattern = "snake_case"
}

rule "terraform_documentation" {
  enabled   = true
  section   = "variables and outputs"
}

rule "terraform_required_version" {
  enabled = true
}

rule "aws_db_instance_storage_encrypted" {
  enabled = true
}

rule "aws_ecr_repository_scan_on_push" {
  enabled = true
}

rule "aws_s3_bucket_public_access_block" {
  enabled = true
}

rule "aws_s3_bucket_versioning" {
  enabled = true
}