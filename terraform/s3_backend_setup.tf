resource "aws_s3_bucket" "terraform_state" {
  bucket = "cocktail-tf-state-${random_id.unique_id.hex}"
  # force_destroy = true
  tags = {
    Name = "Terraform State Bucket"
  }
}

resource "random_id" "unique_id" {
  byte_length = 4
}


resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state_encryption" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}