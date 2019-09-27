def test_file_sysctl_sap_conf(host):
    assert host.file("/etc/sysctl.d/sap.conf").exists
    assert host.file("/etc/sysctl.d/sap.conf").contains("kernel.sem=1250 256000 100 1024")
    assert host.file("/etc/sysctl.d/sap.conf").contains("vm.max_map_count=2000000")
    assert host.sysctl("kernel.sem") == "1250\t256000\t100\t1024"
    assert host.sysctl("vm.max_map_count") == 2000000
