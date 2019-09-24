def test_timed(host):
    assert host.service("chronyd").is_running
    assert host.service("chronyd").is_enabled
