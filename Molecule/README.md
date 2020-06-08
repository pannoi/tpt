# Molecule

## Info

Modular testing at Ansible is the key to making sure the roles work properly. Molecule simplifies this process by allowing you to specify scenarios that test roles in different environments.

Using Ansible from within, Molecule unloads roles to a vendor that deploys a role in a configured environment and calls a verifier (such as Testinfra) to check the drift of the configuration. This ensures that your role has made all the expected changes to the environment in this particular scenario.


> 
Official documentation 
https://molecule.readthedocs.io/en/latest/#

> Use for work:
molecule==2.20
ansible==2.7

## Preparing the environment

The update will ensure that the latest version of the python-pip package, which will install pip and Python, is included in your repository.

```bash
Sudo apt-get update
``` 

pip will be used to create a virtual environment and install additional packages.

```bash
sudo apt-get install -y python-pip
```

Using pip to install the Python module and virtualenv:

```bash
python -m pip install virtualenv
```

Creating and activating a virtual environment:
```bash
python -m virtualenv env_name
```

Activate it to make sure your actions are limited to this environment:
```bash
source env_name/bin/activate
```

Install molecule and docker with pip:
```bash
python -m pip install molecule docker
```

## Creating a role in Molecule
```bash
molecule init role -r role-name -d docker
```
The flag-r indicates the name of the role, while -d indicates the driver that provides hosts for Molecule for use in testing.

To go to the directory of the created role, you need to run the next command:```bash
cd role-name
```

## Configuration file molecule.yml

Before the test starts, Molecule checks the molecule.yml configuration file to make sure everything is in right order. It also prints this test matrix, which determines how the test actions are taken. The test matrix can be seen in the molecule.yml file, which is stored here by default:
> /home/username/role-name/molecule/default/molecule.yml

## Role test

Check the default role to see if the Molecule is set up correctly:
```bash
molecule test
```
The conclusion for testing looks like this:
```bash
Output
--> Validating schema /home/username/role-name/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    ├── lint
    ├── destroy
    ├── dependency
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    └── destroy
...
```
