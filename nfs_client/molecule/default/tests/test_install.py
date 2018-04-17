import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rpcbind_running_and_enabled(host):
    rpcbind = host.service("rpcbind")
    assert rpcbind.is_running
    assert rpcbind.is_enabled
