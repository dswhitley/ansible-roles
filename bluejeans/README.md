Ansible Role: BlueJeans
=======================

This is a role to install the [BlueJeans](https://www.bluejeans.com) desktop
client (this is an video conferencing app).

There is not currently a repository for the client installation.  I am also
unable to decipher what the latest version is.  So unfortunately this role will
specify a version to install.  (I do not want to keep up with this...)

**NOTE** *bluejeans is
[currently not supported](https://support.bluejeans.com/knowledge/bluejeans-app)
 on Ubuntu*

Requirements
------------

* ...

Role Variables
--------------

At some point you may be able to specify a version this role will install, but
currently, it will only install the version specified in
`<role>/defaults/main.yml`

```yaml
...
```

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: bluejeans
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