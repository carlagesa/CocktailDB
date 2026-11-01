resource "aws_ecr_repository" "django_app" {
  name = "django-app"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "django-app"
  }
}

resource "aws_ecr_repository" "nginx" {
  name = "nginx"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "nginx"
  }
}

output "django_app_ecr_url" {
  description = "ECR repository URL for the Django app image"
  value       = aws_ecr_repository.django_app.repository_url
}

output "nginx_ecr_url" {
  description = "ECR repository URL for the nginx image"
  value       = aws_ecr_repository.nginx.repository_url
}