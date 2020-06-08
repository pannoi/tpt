# Terraform 

## Info

Terraform –it is a tool from Hashicorp that helps to manage the infrastructure declaratively. In this case, you don't have to manually create instances, networks, etc. in your cloud provider's console; just write a configuration that tells you how you see your future infrastructure. This configuration is created in a human-readable text format. If you want to change your infrastructure, edit the configuration and launch terraform application. Terraform will send API calls to your cloud provider to align the infrastructure with the configuration in this file.

If you move infrastructure management to text files, you can arm yourself with all your favorite tools for managing the source code and processes, and then refocus them to work with the infrastructure. The infrastructure is now subject to git systems, just like the source code, and can be similarly criticized or rolled back to an earlier state if something goes wrong.


> Official documentation: https://www.terraform.io/docs/index.html

## Installation

You need to install terraform [official provider](https://www.terraform.io/), сnow we're going to use the version: `terraform version == v0.11.11`

Windows

1. Download Terraform `.zip` and extract it Win 10 from [here](https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_windows_amd64.zip);
2. Move extracted .exe file to `C:\Windows\System32\`

Linux

1. Download Terraform `.zip` and extract it Win 10 from [here](https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip);
2. Move extracted file to `/usr/bin`

## Authentication

In order to authenticate in the cloud, with terraform, you need to use an authentication config.

    ```bash
    az login
    ```

## Initialization

The incision process will start installing the hangs and modules that you use in the script
```bash
terraform init
```

## Configure the variables

All variables are stored in  ```variables.tf```, you can adjust them to for  deployment


## Checking status

Terraform creates at the beginning a file called ```*.tfstate``` that stores information about the state of the infrastructure. Using it, you can build up the status of the infrastructure
- Detailed view

  ```bash
  terraform show
  ```

- Simplified view

  ```bash
  terraform state list
  ```

## Planning 

Before you start the script, it's best to see what resources are created/changed/removed. To do this, take advantage of the team and see how the use of the script will change the current infrastructure

    ```bash
    terraform plan
    ```

## Application

Once you've seen that the depot is valid, you can run the script.


    ```bash
    terraform apply
    ```


    ```bash
    terraform apply -auto-approve
    ```

## Conclusions

Inside the platform, you can configure conclusions, for example, from the resources that will be created using a generator (e.g. resource_id)

```bash
terraform output
```

## Destruction 

If you want to remove the infrastructure you've unwrapped with this script, start the command:

```bash
terraform destroy
```

> P.S. Used by the z.tfstate file, make sure it exists
