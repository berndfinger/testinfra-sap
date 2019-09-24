def test_selinux_inactive(host):
    command = host.run("getenforce")
    assert not command.stdout.startswith("Enabled")
