import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rambox_installed(host):
    if host.system_info.distribution == "ubuntu":
        rambox_pkg = "rambox"
    else:
        rambox_pkg = "Rambox"

    assert host.package(rambox_pkg).is_installed
