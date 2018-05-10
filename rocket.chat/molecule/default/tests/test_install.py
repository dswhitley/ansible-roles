import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rocketchat_installed(host):
    rocketchat = host.package("rocketchat")
    assert rocketchat.is_installed
