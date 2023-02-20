"""
1. Introduction to Ansible
- The need:
Efficient management of large-scale infrastructures
Replicated environments
Environment version control
Quick provisioning and recovery

- Other solutions
Chef (Ruby DSL) - Master-agent model, pull-based approach, supports Windows server and node
Puppet (Ruby DSL, Embedded Ruby) - Master-agent model
Salt (YAML) - With or without agents (Salt minions),

- Ansible architecture - YAML, agentless by design, fast communication
Define and track system state -> Managing desired state, Idempotence
Transition from state A to state B -> Provisioning
Automatic execution of tasks on a system
Coordination of automation between systems
Secure by design
Python version 2.7+, 3.5+

2. Working with Ansible
- Inventories and Configurations
Inventory - Static or dynamic, Define and describe the environment
Inventory behavioral parameters
Inventory groups and groups of groups
Group variables
- Using modules - command module (-m command), shell module (-m shell)

command - default, immediately executed
shell - not directly executed, ($HOSTNAME)
script module - executing scripts
Ansible hosts file change ->
ssh-keyscan IP >> ~/.ssh/known_hosts

Config files:
$ANSIBLE_CONFIG
./ansible.cfg
~/.ansible.cfg
/etc/ansible/ansible.cfg

Naming conventions:
dirs: group_vars, host_vars
files: groupname -> vars for group, all(for every group)

3. Advanced Ansible
- Playbook and roles
Playbook -> Set of plays(Single tasks, calling modules), Inventory + Modules
The list way playbook:
- module: kwargs pairs

ansible-playbook playbook_name.yml -> Default inventory
ansible-playbook -i inventory playbook_name.yml

Roles -> Easy sharing of content
/etc/ansible/roles or
roles/ relative to the playbook file(project)
main.yml -> Expected in each folder in dir structure (tasks, handlers, defaults, vars, files, templates, meta)
At least 1 of the folders must be included with main.yml inside

Usage in playbook.yml
roles:
    - service

Ansible Galaxy - Site for sharing roles
command line tool - ansible-galaxy
ansible-galaxy install username.rolename
"""`````````