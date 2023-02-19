"""
1. Infrastructure as Code (IaC)
- Introduction
IaC - Process of managing and provisioning computer data centers through machine-readable
definition files, rather than physical hardware configuration or interactive configuration tools.

2. Terraform basics
Provides flexible abstraction of resources and providers
Covers physical hardware, VMs, containers etc.
A tool for:
- Building infrastructure - Local(on premise), remote(cloud) or hybrid
- Changing
- Versioning

Dry-running before process
- Execution plans - What would be done
- Resource graph - Tracked dependencies

HashiCorp Configuration Language (HCL) -> Interpolation ${var}

Configuration files:
.tf or .tf.json
Content is appended not merged

Override files:
_override
Loaded after the non-override files in alphabetical order
Content is merged

Resources:
Syntax -> resource "type" "resource name" {params}

Data sources:
Used to fetch external information

Providers:
Responsible for the lifecycle of the resources
Multiple providers are allowed

Terraform CLI binary install

New configuration start:
terraform init - Initializing the provider -> .terraform / .terraform.lock.hcl
terraform fmt - Format the file
terraform validate
terraform plan
terraform apply
terraform show - Details about the vm on AWS

* Connecting to the VM using the key pair - Forces replacement,
 terraform apply to destroy the oldVM and create a new one
 Copy key file into the active dir
 terraform console - Resources' attributes
 ssh -i terraform-key.pem ec2-user@Public_IP - Enter the Amazon linux VM

or

put output blocks into the .tf file => The plan gets changed with the outputs -> Terraform.tfstate
*

3. Terraform and Docker
- Dedicated Docker provider
terraform taint type.name -> Resource needs to be replaced
terraform untaint

4. Terraform and AWS
Variable type maps -> Development environment vs Prod environment
terraform workspace list
terraform workspace new production
terraform workspace new development
terraform apply -var 'mode=dev'
terraform workspace select production
terraform apply -var 'mode=prod'
Two running configurations at the same time is possible
terraform workspace delete name

AWS Credentials:
- Static credentials
- Environment credentials
- Shared credentials file
- EC2 Role

Resources:
vpc, gateway, route-table, subnet, route table association, security groups(filter communication in-out, vv.), instance

Running a script in the AWS instance -> Provisioner block in instance block
"""