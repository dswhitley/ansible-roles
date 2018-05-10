Ansible Role: Rocket.Chat
================================

This is a role to install the [Rocket.Chat](https://rocket.chat/) client.

There is not currently a repository for the client installation.  Instead of
making this role version-specific, it will always install the latest version
found here:  https://github.com/RocketChat/Rocket.Chat.Electron/releases/latest

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
    - role: rocket.chat
```



Advanced Configuration
----------------------

The following role variables are dependent on the Visual Studio Code version;
to use a Visual Studio Code version **not pre-configured by this role** you
must configure the variables below:

```yaml
# SHA256 sum for the redistributable package (e.g code_1.3.0-1467909982_amd64.deb)
visual_studio_code_redis_sha256sum: '53eb2cd235b395a28e7fda6f50f904fd5665877e354609f836a6b60a1592c9c9'

# The download URL for the redistributable package
# Permanent download URLs can be found on https://code.visualstudio.com/Updates
visual_studio_code_redis_url: 'https://az764295.vo.msecnd.net/stable/e724f269ded347b49fcf1657fc576399354e6703/code_1.3.0-1467909982_amd64.deb'
```

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: gantsign.visual-studio-code
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