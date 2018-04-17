Ansible Role: nfs_client
========================

Role to install the packages necessary for a system to be an NFS client as well
as create a few mounts if specified.

Requirements
------------

* Ansible >= 2.3 (earlier versions may work but are not tested)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
N/A
```

Mounts are configured as follows:

```yaml
mounts:
  - { src: 1.2.3.4:/share1, dest: /nfs/share1 }
  - { src: 1.2.3.4:/share2, dest: /nfs/anothershare }
```



Advanced Configuration
----------------------

You can specify users who should have a soft link in their home directory 
pointing to the new mounted share.  Simply specify a list of users in 
`home_link` 

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: dswhitley.nfs_client
```

Playbook with extensions installed:

```yaml
- hosts: localhost
  connection: local
  roles:
    - role: dswhitley.nfs_client
      mounts:
        - { src: "1.2.3.4:/share1", dest: "/nfs/share1" }
        - { src: "1.2.3.4:/share2", dest: "/nfs/anothershare" }
        - { src: "1.2.3.4:/share3", dest: "/nfs/anothershare2" }
      home_link:
        - "{{ new_user | default( ansible_user_id ) }}"
        - anotheruser
```

More Roles From dswhitley
-------------------------

You can find more roles in my 
[ansible-roles](https://github.com/dswhitley/ansible-roles) repository.

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

This particular role is hard to test if mounts are passed during invocation.  
Therefore, the testing that has been done is focused on installing the correct 
packages and ensuring the correct services are started.

ADDITIONALLY: containers don't inherently have use systemd so testing services
that use systemd are troublesome.  [This](https://medium.com/@tklo/testing-ansible-role-of-a-systemd-based-service-using-molecule-and-docker-4b3608a10ef0)
page should help, it is what I've used to test CentOS and Fedora containers and
this role...but it is still failing for Ubuntu.  Ship it.

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

Daniel Whitley
