def test_file_limits_sap_conf(host):
    assert host.file("/etc/security/limits.d/99-sap.conf").exists
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys\thard\tnproc\tunlimited")
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys\tsoft\tnproc\tunlimited")
