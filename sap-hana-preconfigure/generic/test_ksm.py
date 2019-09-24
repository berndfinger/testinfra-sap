def test_ksm(host):
    assert host.file("/etc/init.d/boot.local").exists
    assert host.file("/etc/init.d/boot.local").contains("echo 0 > /sys/kernel/mm/ksm/run")
    command = host.run("cat /sys/kernel/mm/ksm/run")
    assert command.stdout.startswith("0")
