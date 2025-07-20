resource "random_password" "rds_password" {
  length  = 16
  special = true
}

resource "random_id" "secret_suffix" {
  byte_length = 4
}

resource "aws_secretsmanager_secret" "rds_password" {
  name = "rds-password-${random_id.secret_suffix.hex}"
}

resource "aws_secretsmanager_secret_version" "rds_password" {
  secret_id     = aws_secretsmanager_secret.rds_password.id
  secret_string = random_password.rds_password.result
}

resource "aws_db_subnet_group" "production" {
  name       = "main-tf"
  subnet_ids = [aws_subnet.private-subnet-1.id, aws_subnet.private-subnet-2.id]
}

resource "aws_db_instance" "production" {
  identifier              = "production"
  db_name                 = var.rds_db_name
  username                = var.rds_username
  password                = random_password.rds_password.result
  port                    = "5432"
  engine                  = "postgres"
  engine_version          = "17"
  instance_class          = var.rds_instance_class
  allocated_storage       = "20"
  storage_encrypted       = false
  vpc_security_group_ids  = [aws_security_group.rds.id]
  db_subnet_group_name    = aws_db_subnet_group.production.name
  multi_az                = false
  storage_type            = "gp2"
  publicly_accessible     = false
  backup_retention_period = 7
  skip_final_snapshot     = true
}