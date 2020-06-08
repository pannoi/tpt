# Ansible

## Info

Ansible is a very flexible and easy tool for writing scripts to automation scenarios of any complexity. You can describe in it how a simple developer environment so complex large multi-environment project (dev/stage/prod).

> Official documentation:  http://docs.ansible.com/
# Installation

> Ubuntu

First, you need to update the list of packages to guaranteed get the latest version of the Ansible we need
```bash
sudo apt update
```
It is also worth updating the packages already installed
```bash
sudo apt upgrade
```

Now install Ansible
```bash
sudo apt install ansible
```
To verify that Ansible has been installed, follow the following command:
```bash
ansible --versioon
```

All blocks in Ansible, be it playbooks or vars (variables), start with what we prescribe in the first line of the file:
```bash
---
```
# Playbooks

Ansible playbooks are a way to send commands to remote computers using scripts. Instead of individually using Ansible commands to remotely customize computers from the command line, you can customize entire complex environments by passing the script to one or more systems.

File extension, whether it's playbook/tasks/variable (vars), is .yml

> Block structure in file playbook.yml
```bash
---
- name: Install Packages
  hosts: all
  become: true
  roles:
    - role: tpt
```

## Tasks

Ansible tasks - are tasks that will be performed by Ansible, by the type of installation of packages, launch services, unpacking, copying and the like. Examples of shuffles can be found in the roles/tpt/tasks section of this documentation.

An example of a block in a task to install packages recorded in variable packages
```bash
    - name: Install apcahe+php modules 
      apt:
          name: "{{ item }}" 
          update_cache: yes
          state: latest
      with_items: "{{ packages }}"
```

> You can read all the modules here: 
https://docs.ansible.com/ansible/2.3/list_of_all_modules.html

## Roles

It's a way to group multiple tasks into one container to effectively automate your work using an understandable directory structure. 
Role structure:
```bash
/home/user/ansible:
    playbook.yml
    roles:
        tpt:
            tasks:
                main.yml
            vars:
                main.yml
```
>In the vars folder, in the main.yml file, you can specify variables that can store information, such as a list of applications, text, etc. /vars/main.yml
With an example of variables can be found in the roles section/tpt/vars in this documentation.


 



