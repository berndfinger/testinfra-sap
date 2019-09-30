def test_coredumps_disabled(host):
    assert host.file("/etc/security/limits.d/99-sap.conf").exists
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("*\thard\tcore\t0")
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("*\tsoft\tcore\t0")
