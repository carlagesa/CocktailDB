# OIDC role for GitHub Actions
#
# Create this role in the target AWS account, then configure it as the
# `AWS_ROLE_TO_ASSUME` secret in GitHub (format: arn:aws:iam::<account-id>:role/<name>).
#
# The trust policy below allows GitHub Actions to assume the role only from
# this repository, on the `main` branch, for the production environment.

data "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"
}

resource "aws_iam_role" "github_actions" {
  name = "github-actions-ci-cd"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Federated = data.aws_iam_openid_connect_provider.github.arn
        }
        Condition = {
          StringEquals = {
            "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"
            "token.actions.githubusercontent.com:sub" = "repo:carlagesa/CocktailDB:ref:refs/heads/main"
          }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "ci_cd" {
  name = "ci-cd-policy"
  role = aws_iam_role.github_actions.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ecr:GetAuthorizationToken",
          "ecr:BatchCheckImageAvailability",
          "ecr:CompleteLayerUpload",
          "ecr:GetAuthorizationToken",
          "ecr:UploadLayerPart",
          "ecr:ListImages",
          "ecr:BatchDeleteImage",
          "ecr:PutImage",
          "ecr:InitiateLayerUpload",
          "ecr:GetDownloadUrlForLayer",
          "ecr:DescribeRepositories",
          "ecr:BatchGetImage",
          "ecr:UploadLayerPart"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "ecs:DescribeServices",
          "ecs:DescribeTaskDefinition",
          "ecs:DescribeTasks",
          "ecs:ListServices",
          "ecs:ListTasks",
          "ecs:ListTaskDefinitionFamilies",
          "ecs:ListDefinitions",
          "ecs:RegisterTaskDefinition",
          "ecs:UpdateService",
          "ecs:RunTask",
          "ecs:StopTask",
          "ecs:WaitServicesStable"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "iam:PassRole"
        ]
        Resource = [
          aws_iam_role.ecs-task-execution-role.arn
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket",
          "s3:DeleteObject"
        ]
        Resource = [
          "arn:aws:s3:::cocktail-tf-state",
          "arn:aws:s3:::cocktail-tf-state/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue"
        ]
        Resource = [
          "arn:aws:secretsmanager:*:*:secret:rds-password-*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "sts:GetCallerIdentity",
          "sts:GetFederationToken"
        ]
        Resource = "*"
      }
    ]
  })
}

output "github_actions_role_arn" {
  description = "ARN of the OIDC role assumed by GitHub Actions"
  value       = aws_iam_role.github_actions.arn
}