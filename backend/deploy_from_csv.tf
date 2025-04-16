terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

data "csvdecode" "master_plan" {
  file = "${path.module}/../tables/master_plan_v3.2.csv"
}

resource "aws_iam_role" "agent_roles" {
  for_each = { for idx, row in data.csvdecode.master_plan.records : 
              row.Component => row if contains(["API Auth", "Cost Management"], row.Component) }

  name               = "agentic-${lower(each.key)}-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_appautoscaling_target" "agent_scale" {
  for_each           = data.csvdecode.master_plan.records
  service_namespace  = "lambda"
  scalable_dimension = "lambda:function:ProvisionedConcurrency"
  min_capacity       = each.value.Automation_Level * 2
  max_capacity       = each.value.Automation_Level * 10
}
