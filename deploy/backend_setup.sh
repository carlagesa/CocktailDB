#!/bin/bash

# This script checks if the S3 bucket for Terraform state exists.
# If it doesn't exist, it creates it.
# This prevents the CI/CD pipeline from failing if the bucket already exists.

set -e

# == CONFIGURATION ==
# The name of the S3 bucket to use for Terraform state.
# This should match the 'bucket' value in your terraform/backend.tf file.
BUCKET_NAME="cocktail-tf-state"

# The AWS region where the bucket should be created.
# This should match the 'region' value in your terraform/backend.tf file.
AWS_REGION="us-east-1"
# ===================

# Check if the bucket exists using head-bucket
if aws s3api head-bucket --bucket "$BUCKET_NAME" 2>/dev/null; then
  echo "Terraform state bucket '$BUCKET_NAME' already exists. Skipping creation."
else
  echo "Terraform state bucket '$BUCKET_NAME' does not exist. Creating bucket..."
  aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$AWS_REGION"
  
  echo "Enabling server-side encryption for bucket '$BUCKET_NAME'..."
  aws s3api put-bucket-encryption \
    --bucket "$BUCKET_NAME" \
    --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
  
  echo "Bucket '$BUCKET_NAME' created and configured successfully."
fi