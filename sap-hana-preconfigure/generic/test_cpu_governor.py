def test_cpu_governor(host):
    command = host.run("cpupower frequency-info -g | awk '/available cpufreq governors/{print $(NF-1), $NF}'")
    if not command.stdout.startswith("Not Available"):
        assert host.file("/etc/rc.d/rc.local").exists
        assert host.file("/etc/rc.d/rc.local").contains("cpupower frequency-set -g performance")

