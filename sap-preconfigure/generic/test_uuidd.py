def test_uuidd_running_and_enabled(host):
    uuidd = host.service("uuidd")
    assert uuidd.is_running
    assert uuidd.is_enabled
