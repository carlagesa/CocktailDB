resource "aws_iam_role" "network_switch_lambda_role" {
  name = "network-switch-lambda-role"

  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Action    = "sts:AssumeRole",
        Effect    = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy" "network_switch_lambda_policy" {
  name        = "network-switch-lambda-policy"
  description = "Policy for Network Switch Lambda function"

  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Action = [
          "ecs:UpdateService",
          "ecs:DescribeServices"
        ],
        Effect   = "Allow",
        Resource = "*"
      },
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Effect   = "Allow",
        Resource = "arn:aws:logs:*:*:*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "network_switch_lambda_attachment" {
  role       = aws_iam_role.network_switch_lambda_role.name
  policy_arn = aws_iam_policy.network_switch_lambda_policy.arn
}

data "archive_file" "network_switch_lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda_function.py"
  output_path = "${path.module}/lambda_function.zip"
}

resource "aws_lambda_function" "network_switch_lambda" {
  filename      = data.archive_file.network_switch_lambda_zip.output_path
  function_name = "network-switch-handler"
  role          = aws_iam_role.network_switch_lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  source_code_hash = data.archive_file.network_switch_lambda_zip.output_base64sha256
  runtime       = "python3.8"
  timeout       = 300

  environment {
    variables = {
      ECS_CLUSTER_NAME = var.ecs_cluster_name
      ECS_SERVICE_NAME = var.ecs_service_name
      PUBLIC_SUBNETS   = join(",", var.public_subnet_ids)
      PRIVATE_SUBNETS  = join(",", var.private_subnet_ids)
      SECURITY_GROUPS  = join(",", var.security_group_ids)
    }
  }
}