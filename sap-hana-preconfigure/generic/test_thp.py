def test_thp_disabled(host):
    assert host.file("/etc/default/grub").contains("transparent_hugepage=never")
