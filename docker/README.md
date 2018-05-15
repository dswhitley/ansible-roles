Ansible Role: Terminator
========================

Role to install the [Terminator](https://gnometerminator.blogspot.com/)
terminal emulator.  I am choosing this in the hopes that I can easily modify
settings because it is one of the very few emulators that uses text files
instead of dconf for settings.  This means I can simply copy a config file to a
newly deployed system instead of trying to modify the dbus database for
specific users which is a real nightmare.

This will be installed via various repositories and therefore updated similarly
so the exact version does not need to be specified.

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
    - role: terminator
```

**NOTE** *I'd like to extend this role so that you can specify different
options per user potentially using a very generic template, but I have not figured that out yet.  Currently, I am just copying a generic configuration
file to each user's directory.*

Playbook with configuration options specified:

```yaml
- hosts: servers
  roles:
    - role: terminator
      users:
        - username: "{{ new_user | default( ansible_user_id ) }}"
          terminator_default_profile_settings:
            - { key: "background_color", value: "#2d2d2d" }
            - { key: "background_darkness", value: "0.95" }
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