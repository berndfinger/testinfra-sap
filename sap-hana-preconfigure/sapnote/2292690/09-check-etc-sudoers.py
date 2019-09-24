def test_etc_sudoers(host):
    assert not host.file("/etc/sudoers").contains("Defaults requiretty")
