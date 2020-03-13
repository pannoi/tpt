variable "subscription" {
  default = "051327ce-f0cb-4676-acfc-09d680efe40f"
  description = "Specify subscription id localy, do not push it"
}

variable "rgName" {
  default = "sampleRG"
  description = "Name of resource group"
}

variable "region" {
  default = "West Europe"
  description = "Name of location, where resources are going to be provisioned"
}

variable "containerName" {
  default = "python"
}

