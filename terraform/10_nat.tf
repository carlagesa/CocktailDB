module "disposable_nat_gateway" {
  source = "./modules/disposable-nat-gateway"

  private_subnet_id      = aws_subnet.private-subnet-1.id
  public_subnet_id       = aws_subnet.public-subnet-1.id
  private_route_table_id = aws_route_table.private-route-table.id
  ecs_cluster_arn        = aws_ecs_cluster.production.arn
}