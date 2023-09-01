variable "account_ids" {
  description = "List of AWS account IDs to apply customizations to"
  type        = list(string)
  default     = []
}

variable "aws_partition" {
  description = "AWS partition to use"
  type        = string
  default     = "aws"
}

variable "aft_home_region" {
  description = "AWS region to use for AFT home region"
  type        = string
}