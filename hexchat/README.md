Ansible Role: hexchat
=====================

This is a role to install the [hexchat](https://hexchat.github.io/) IRC client.

This will be installed via various repositories and therefore updated similarly
so the exact version does not need to be specified.

I am attempting to allow a basic configuration via passing variables to the role
but have thusfar been unable to figure out how to assign default channels...but
I just don't know much about IRC at this point.

If settings are tweaked in the future, simply modify the appropriate template
file.

Requirements
------------

* ...

Role Variables
--------------

The variables you can pass into this role are really specific to configuration
at this point.  The role is designed so that you can specify different options
for different users.  However, simply using the role with no variables will just
install the client and apply no configuration (so all variables are optional).

* `username:` a username for which to apply the rest of the settings *this is
required if any other options are passed*
* `irc_nick:` the nickname to use in the client
* `servers:` a **list** of servers to connect to by default (the network will be
created based on `username`)
* `channels:` this is currently not used, but is included as a way to document
(remind yourself) which channels you should join

**NOTE** *this role will not create the users specified, it is assumed that that
will be handled elsewhere*

Example Playbooks
-----------------

Minimal playbook:

```yaml
- hosts: servers
  roles:
    - role: hexchat
```

Playbook with user-specific settings:
```yaml
- hosts: servers
  roles:
    - role: hexchat
      users:
        - username: "{{ new_user | default( ansible_user_id ) }}"
          irc_nick: "{{ new_nick }}"
          servers:
            - irc.server1.com/6667
            - irc.server2.com/6667
          channels:
            - noob
        - username: user2
          irc_nick: iamuser2
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