data "aws_ssm_parameter" "ecs_optimized_ami" {
  name = "/aws/service/ecs/optimized-ami/amazon-linux-2/recommended/image_id"
}

resource "aws_launch_template" "ecs_spot" {
  name_prefix   = "ecs-spot-"
  image_id      = data.aws_ssm_parameter.ecs_optimized_ami.value
  instance_type = "t3.micro"

  iam_instance_profile {
    name = aws_iam_instance_profile.ecs-instance-profile.name
  }

  network_interfaces {
    associate_public_ip_address = false
    security_groups             = [aws_security_group.ecs-ec2.id]
  }

  user_data = base64encode(<<-EOF
              #!/bin/bash
              echo "ECS_CLUSTER=${aws_ecs_cluster.production.name}" >> /etc/ecs/ecs.config
              EOF
  )

  instance_market_options {
    market_type = "spot"
  }
}

resource "aws_autoscaling_group" "ecs_spot" {
  name                = "ecs-spot-asg"
  vpc_zone_identifier = [aws_subnet.private-subnet-1.id, aws_subnet.private-subnet-2.id]
  desired_capacity    = 1
  max_size            = 10
  min_size            = 1

  launch_template {
    id      = aws_launch_template.ecs_spot.id
    version = "$Latest"
  }

  tag {
    key                 = "AmazonECSManaged"
    value               = true
    propagate_at_launch = true
  }
}

resource "aws_appautoscaling_target" "ecs_target" {
  max_capacity       = var.autoscale_max
  min_capacity       = var.autoscale_min
  resource_id        = "service/${aws_ecs_cluster.production.name}/${aws_ecs_service.production.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}

resource "aws_appautoscaling_policy" "ecs_policy" {
  name               = "ecs-auto-scaling-policy"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.ecs_target.resource_id
  scalable_dimension = aws_appautoscaling_target.ecs_target.scalable_dimension
  service_namespace  = aws_appautoscaling_target.ecs_target.service_namespace

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }

    target_value       = 75
    scale_in_cooldown  = 300
    scale_out_cooldown = 300
  }
}

# ECS service auto scaling

variable "autoscale_min" {
  description = "Minimum autoscale (number of tasks)"
  default     = "1"
}

variable "autoscale_max" {
  description = "Maximum autoscale (number of tasks)"
  default     = "10"
}

variable "autoscale_desired" {
  description = "Desired number of tasks to run initially"
  default     = "4"
}