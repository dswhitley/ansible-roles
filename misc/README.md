Ansible Role: misc
==================

Unfortunately I have just gotten lazy and decided to lump a bunch of stuff into
a "misc" role instead of creating and testing the appropriate cross-platform
roles.  My **intention** is to pull all these tasks out into appropriate roles
but only time will tell if that comes to be.

My daily driver is a Fedora system, so initially most of this will mainly be
relevant to Fedora systems.

I won't be testing this role with `molecule` but I have left the directory 
structure in place for posterities sake. There will be plenty of room for
improvements here...

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
    - role: misc
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