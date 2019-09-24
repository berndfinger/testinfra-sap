def test_etc_tmpfiles_d_sap_conf_exists(host):
    assert host.file("/etc/tmpfiles.d/sap.conf").exists
