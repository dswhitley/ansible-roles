import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_slack_installed(host):
    if host.system_info.distribution == "ubuntu":
        slack_pkg = "slack-desktop"
    else:
        slack_pkg = "slack"

    assert host.package(slack_pkg).is_installed
