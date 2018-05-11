import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_scudcloud_installed(host):
    scudcloud = host.package("scudcloud")
    assert scudcloud.is_installed
