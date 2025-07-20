resource "aws_iam_role" "nat_lambda_role" {
  name = "nat-lambda-role"

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

resource "aws_iam_policy" "nat_lambda_policy" {
  name        = "nat-lambda-policy"
  description = "Policy for NAT Lambda function"

  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Action = [
          "ec2:CreateNetworkInterface",
          "ec2:DescribeNetworkInterfaces",
          "ec2:DeleteNetworkInterface",
          "ec2:CreateTags",
          "ec2:DeleteTags",
          "ec2:DescribeSubnets",
          "ec2:DescribeRouteTables",
          "ec2:CreateRoute",
          "ec2:DeleteRoute",
          "ec2:ReplaceRoute"
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

resource "aws_iam_role_policy_attachment" "nat_lambda_attachment" {
  role       = aws_iam_role.nat_lambda_role.name
  policy_arn = aws_iam_policy.nat_lambda_policy.arn
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda_function.py"
  output_path = "${path.module}/lambda_function.zip"
}

resource "aws_lambda_function" "nat_lambda" {
  filename      = data.archive_file.lambda_zip.output_path
  function_name = "nat-gateway-handler"
  role          = aws_iam_role.nat_lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime       = "python3.8"
  timeout       = 300

  environment {
    variables = {
      PRIVATE_SUBNET_ID = var.private_subnet_id
      PUBLIC_SUBNET_ID  = var.public_subnet_id
      ROUTE_TABLE_ID    = var.private_route_table_id
    }
  }
}

resource "aws_cloudwatch_event_rule" "ecs_task_rule" {
  name        = "ecs-task-state-change-rule"
  description = "Capture ECS task state changes"

  event_pattern = jsonencode({
    source      = ["aws.ecs"],
    "detail-type" = ["ECS Task State Change"],
    detail      = {
      clusterArn = [var.ecs_cluster_arn]
    }
  })
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.ecs_task_rule.name
  target_id = "nat-lambda-target"
  arn       = aws_lambda_function.nat_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.nat_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.ecs_task_rule.arn
}