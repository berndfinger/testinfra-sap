def test_nproc(host):
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys    hard    nproc    unlimited")
    assert host.file("/etc/security/limits.d/99-sap.conf").contains("@sapsys    soft    nproc    unlimited")
