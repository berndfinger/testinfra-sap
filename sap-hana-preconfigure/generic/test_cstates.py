def test_cstates(host):
    assert host.file("/etc/default/grub").contains("processor.max_cstate=1")
    assert host.file("/etc/default/grub").contains("intel_idle.max_cstate=1")
