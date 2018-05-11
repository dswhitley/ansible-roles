Ansible Role: Rambox
====================

**UPDATE**  *We use SSO for Rocket.Chat and that is 
[not working](https://github.com/saenzramiro/rambox/issues/1005) in Rambox...so
this is here for historical purposes, I will be installing the clients 
individually*

This is a role to install [Rambox](https://rambox.pro/) which is an app that
combines common web applications into one.  I understand that this is really
nothing more than a single purpose, stripped down web browser, but I _THINK_
that I like that you are able to sync your configuration across different (or
newly installed) computers.  This will replace the need to install a client for
[Slack](https://slack.com/downloads/linux) (or an FOSS alternative such as 
[scudcloud](https://github.com/raelgc/scudcloud)) AND a client for 
[Rocket.Chat](https://rocket.chat/)...

There is not currently a repository for the client installation.  Instead of
making this role version-specific, it will always install the latest version
found here:  https://github.com/saenzramiro/rambox/releases/latest

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
    - role: rambox
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