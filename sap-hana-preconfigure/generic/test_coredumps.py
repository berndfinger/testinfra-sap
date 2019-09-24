def test_coredumps_disabled(host):
    assert host.file("/etc/security/limits.d/99-sap.conf").exists
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("hard core 0")
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("soft core 0")
