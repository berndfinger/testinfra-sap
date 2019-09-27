def test_vm_max_map_count(host):
    assert host.file("/etc/sysctl.d/sap.conf").exists
    assert host.file("/etc/sysctl.d/sap.conf").contains("vm.max_map_count=2147483647")
    assert host.sysctl("vm.max_map_count") == 2147483647

