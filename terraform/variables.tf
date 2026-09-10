variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "frontend_port" {
  description = "Frontend external port"
  type        = number
}

variable "backend_port" {
  description = "Backend external port"
  type        = number
}