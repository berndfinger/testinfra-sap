def test_firewalld_inactive_and_disabled(host):
    firewalld = host.service("firewalld")
    assert not firewalld.is_running
    assert not firewalld.is_enabled

