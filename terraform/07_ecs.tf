resource "aws_ecs_capacity_provider" "spot" {
  name = "spot-capacity-provider"
  auto_scaling_group_provider {
    auto_scaling_group_arn         = aws_autoscaling_group.ecs_spot.arn
    managed_termination_protection = "ENABLED"

    managed_scaling {
      status          = "ENABLED"
      target_capacity = 100
    }
  }
}

resource "aws_ecs_cluster_capacity_providers" "cluster_attachment" {
  cluster_name = aws_ecs_cluster.production.name

  capacity_providers = [aws_ecs_capacity_provider.spot.name]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = aws_ecs_capacity_provider.spot.name
  }
}

resource "aws_ecs_cluster" "production" {
  name = "${var.ecs_cluster_name}-cluster"
}

data "template_file" "app" {
  template = file("templates/django_app.json.tpl")

  vars = {
    docker_image_url_django = var.docker_image_url_django
    docker_image_url_nginx  = var.docker_image_url_nginx
    region                  = var.region
    rds_db_name             = var.rds_db_name
    rds_username            = var.rds_username
    rds_password_arn        = aws_secretsmanager_secret.rds_password.arn
    rds_hostname            = aws_db_instance.production.address
    nginx_conf_hash         = filesha256("../nginx/nginx.conf")
  }
}

resource "aws_ecs_task_definition" "app" {
  family                = "django-app"
  network_mode          = "awsvpc"
  execution_role_arn    = aws_iam_role.ecs-task-execution-role.arn
  task_role_arn         = aws_iam_role.ecs-task-execution-role.arn
  container_definitions = data.template_file.app.rendered
}

resource "aws_ecs_task_definition" "django_migration" {
  family             = "django-migration-task"
  network_mode       = "awsvpc"
  execution_role_arn = aws_iam_role.ecs-task-execution-role.arn
  task_role_arn      = aws_iam_role.ecs-task-execution-role.arn

  container_definitions = jsonencode([
    {
      name      = "django-migration-container",
      image     = var.docker_image_url_django,
      memory    = 512,
      command   = ["python", "manage.py", "migrate"],
      secrets   = [
        {
          name      = "RDS_PASSWORD",
          valueFrom = aws_secretsmanager_secret.rds_password.arn
        }
      ],
      environment = [
        {
          name  = "RDS_DB_NAME",
          value = var.rds_db_name
        },
        {
          name  = "RDS_USERNAME",
          value = var.rds_username
        },
        {
          name  = "RDS_HOSTNAME",
          value = aws_db_instance.production.address
        },
        {
          name  = "RDS_PORT",
          value = "5432"
        }
      ],

      logConfiguration = {
        logDriver = "awslogs",
        options = {
          awslogs-group         = "/ecs/django-app",
          awslogs-region        = var.region,
          awslogs-stream-prefix = "ecs"
        }
      },

      portMappings = [
        {
          containerPort = 8000,
          protocol      = "tcp"
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "production" {
  name            = "${var.ecs_cluster_name}-service"
  cluster         = aws_ecs_cluster.production.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = var.app_count
  launch_type     = "EC2"

  load_balancer {
    target_group_arn = aws_alb_target_group.default-target-group.arn
    container_name   = "nginx"
    container_port   = 80
  }

  network_configuration {
    subnets         = [aws_subnet.private-subnet-1.id, aws_subnet.private-subnet-2.id]
    security_groups = [aws_security_group.ecs-fargate.id]
  }

  depends_on = [aws_ecs_cluster_capacity_providers.cluster_attachment]
}

# ecs

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "production"
}

variable "docker_image_url_django" {
  description = "Docker image to run in the ECS cluster"
  default     = "626690050115.dkr.ecr.us-east-1.amazonaws.com/django-app:latest"
}

# nginx

variable "docker_image_url_nginx" {
  description = "Docker image to run in the ECS cluster"
  default     = "626690050115.dkr.ecr.us-east-1.amazonaws.com/nginx:latest"
}

variable "app_count" {
  description = "Number of Docker containers to run"
  default     = 2
}


