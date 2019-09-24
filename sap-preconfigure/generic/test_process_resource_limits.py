def test_file_limits_sap_conf(host):
    assert host.file("/etc/security/limits.d/99-sap.conf").exists
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys    hard    nofile    32800")
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys    soft    nofile    32800")
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys    soft    nproc    unlimited")
