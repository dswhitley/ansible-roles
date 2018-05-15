import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_new_user(host):
    user = host.user("test_user1")
    assert user.exists
    assert user.name == "test_user1"
    assert user.uid == 1000
    assert user.gid == 1000
