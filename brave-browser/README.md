Ansible Role: Brave browser
================================

Role to install the [Brave](https://brave.com/index/) browser.  This will be 
installed via a repository and therefore updated similarly so the exact version
does not need to be specified.

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
    - role: brave-browser
```

Playbook with extensions installed:

```yaml
- hosts: servers
  roles:
    - role: gantsign.visual-studio-code
      users:
        - username: vagrant
          visual_studio_code_extensions:
            - streetsidesoftware.code-spell-checker
            - wholroyd.jinja
            - donjayamanne.python
          visual_studio_code_settings: {
            "editor.rulers": [80, 100, 120],
            "editor.renderWhitespace": true,
            "files.associations": {
              "Vagrantfile": "ruby"
            }
          }
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