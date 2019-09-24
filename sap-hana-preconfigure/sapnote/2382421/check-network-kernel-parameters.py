def test_network_kernel_parameters(host):
    assert host.sysctl("net.core.somaxconn") == 4096
    assert host.sysctl("net.ipv4.tcp_max_syn_backlog") == 8192
    assert host.sysctl("net.ipv4.tcp_timestamps") == 1
    assert host.sysctl("net.ipv4.tcp_slow_start_after_idle") == 0
