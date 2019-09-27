def test_epb(host):
    command = host.run("cpupower info | head -1 | awk '{print $2, $3, $4}'")
    if not command.stdout.startswith("does not support"):
        assert host.file("/etc/init.d/boot.local").exists
        assert host.file("/etc/init.d/boot.local").contains("cpupower set -b 0")
        command2 = host.run("cpupower info -b | grep -A 2 \"analyzing CPU 0:\" | tail -1")
        assert command2.stdout.startswith("perf-bias: 0")
