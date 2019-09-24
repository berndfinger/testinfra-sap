def test_kdump_stopped_and_disabled(host):
    kdump = host.service("kdump")
    assert not kdump.is_running
    assert not kdump.is_enabled
