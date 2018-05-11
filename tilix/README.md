Ansible Role: Tilix
================================

Role to install the [Tilix](https://gnunn1.github.io/tilix-web/) terminal
emulator.  I am choosing this in the hopes that I can easily modify settings
with dconf and have multiple tiles/tabs for various terminals.  

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
    - role: tilix
```

Playbook with configuration options specified:

```yaml
- hosts: servers
  roles:
    - role: tilix
      users:
        - username: "{{ new_user | default( ansible_user_id ) }}"
          tilix_settings: 
            - { key: "/dconf/path1/", value: "value1" }
            - { key: "/dconf/path2/", value: "value2" }
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