provider "azurerm" {
  subscription_id = "${var.subscription}"
  version = "v1.44.0"
}

resource "azurerm_resource_group" "resourceGroup" {
  name     = "${var.rgName}"
  location = "${var.region}"
}

// This module create random ID, it is needed to generate storage account name, which must be unique
resource "random_id" "randomId" {
  keepers = {
    resource_group_name = "${azurerm_resource_group.resourceGroup.name}"
  }
  byte_length = 8
}
resource "azurerm_storage_account" "storageAccount" {
  name = "tpt${random_id.randomId.hex}"
  resource_group_name = "${azurerm_resource_group.resourceGroup.name}"
  location = "${azurerm_resource_group.resourceGroup.location}"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "tptContainer" {
  name                  = "${var.containerName}"
  storage_account_name  = "${azurerm_storage_account.storageAccount.name}"
  container_access_type = "private"
}

############
# HOMEWORK #
############

/*
Create virtual machine with Linux Distribution
Script will be updated
*/

