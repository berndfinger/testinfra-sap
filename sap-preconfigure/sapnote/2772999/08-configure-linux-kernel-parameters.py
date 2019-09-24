def test_file_etc_sysctl_d_sap_conf(host):
    assert host.file("/etc/sysctl.d/sap.conf").exists
    assert host.file("/etc/sysctl.d/sap.conf").contains("vm.max_map_count = 2147483647")
