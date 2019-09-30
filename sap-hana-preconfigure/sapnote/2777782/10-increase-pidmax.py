def test_pid_max(host):
    assert host.file("/etc/sysctl.d/sap.conf").exists
    assert host.file("/etc/sysctl.d/sap.conf").contains("kernel.pid_max=4194304")
    assert host.sysctl("kernel.pid_max") == 4194304
