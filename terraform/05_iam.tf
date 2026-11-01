resource "aws_iam_role" "ecs-task-execution-role" {
  name               = "ecs_task_execution_role_prod"
  assume_role_policy = file("policies/ecs-role.json")
}

resource "aws_iam_role_policy" "ecs-task-execution-role-policy" {
  name   = "ecs_task_execution_role_policy"
  policy = file("policies/ecs-task-execution-policy.json")
  role   = aws_iam_role.ecs-task-execution-role.id
}

resource "aws_iam_policy" "ecs_secrets_policy" {
 name        = "ecs_secrets_policy"
 description = "Policy to allow ECS tasks to access secrets"

 policy = jsonencode({
   Version = "2012-10-17"
   Statement = [
     {
       Action = [
         "secretsmanager:GetSecretValue",
       ]
       Effect   = "Allow"
       Resource = aws_secretsmanager_secret.rds_password.arn
     },
   ]
 })
}

resource "aws_iam_role_policy_attachment" "ecs_secrets_attachment" {
 role       = aws_iam_role.ecs-task-execution-role.name
 policy_arn = aws_iam_policy.ecs_secrets_policy.arn
}

resource "aws_iam_role" "ecs-service-role" {
 name               = "ecs_service_role_prod"
 assume_role_policy = file("policies/ecs-role.json")
}

resource "aws_iam_role_policy" "ecs-service-role-policy" {
  name   = "ecs_service_role_policy"
  policy = file("policies/ecs-service-role-policy.json")
  role   = aws_iam_role.ecs-service-role.id
}

resource "aws_iam_role" "ecs-instance-role" {
  name               = "ecs-instance-role-prod"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs-instance-role-attachment" {
  role       = aws_iam_role.ecs-instance-role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

resource "aws_iam_instance_profile" "ecs-instance-profile" {
  name = "ecs-instance-profile-prod"
  role = aws_iam_role.ecs-instance-role.name
}