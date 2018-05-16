import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bluejeans_installed(host):
    if host.system_info.distribution != "ubuntu":
        bluejeans = host.package("bluejeans")
        assert bluejeans.is_installed
