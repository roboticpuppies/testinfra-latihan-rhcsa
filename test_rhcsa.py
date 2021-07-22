#!/usr/bin/env python3

import pytest

with open("inventories/test_server.yml", "r") as f:
    testinfra_hosts = f.read().splitlines()

# Check if Selinux is in Permissive mode
def test_selinux(host):
    cmd = host.run("/usr/sbin/getenforce")
    assert cmd.stdout == "Permissive\n"

# More to do