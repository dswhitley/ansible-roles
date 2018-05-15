Ansible Role: local-users
=========================

Role to create specified users.  There are many situations where the new_user
will be perfectly fine being local.  So we will create this local user early
on in the Ansible process.

I am generically setting the password to be the same as the user and
requiring a password change upon first login.

This username will be added to the sudoers file to allow for password-less
sudo access.

Requirements
------------

* ...

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
...
```


Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: local-users
      new_user: <new_username>
```

More Roles From dswhitley
-------------------------

You can find more roles from dswhitley on
[GitHub](https://github.com/dswhitley/ansible-roles).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

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