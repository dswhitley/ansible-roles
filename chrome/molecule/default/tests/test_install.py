import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chrome_is_installed(host):
    chrome = host.package("google-chrome-stable")
    assert chrome.is_installed
