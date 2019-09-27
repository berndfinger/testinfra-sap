def test_network_kernel_parameters(host):
    assert host.file("/etc/sysctl.d/ibm_largesend.conf").exists
    assert host.file("/etc/sysctl.d/ibm_largesend.conf").contains("net.core.rmem_max=56623104")
    assert host.file("/etc/sysctl.d/ibm_largesend.conf").contains("net.core.wmem_max=56623104")
    assert host.file("/etc/sysctl.d/ibm_largesend.conf").contains("net.ipv4.tcp_rmem=65536 262088 56623104")
    assert host.file("/etc/sysctl.d/ibm_largesend.conf").contains("net.ipv4.tcp_wmem=65536 262088 56623104")
    assert host.file("/etc/sysctl.d/ibm_largesend.conf").contains("net.ipv4.tcp_mem=56623104 56623104 56623104")
    assert host.sysctl("net.core.rmem_max") == 56623104
    assert host.sysctl("net.core.wmem_max") == 56623104
    assert host.sysctl("net.ipv4.tcp_rmem") == "65536\t262088\t56623104"
    assert host.sysctl("net.ipv4.tcp_wmem") == "65536\t262088\t56623104"
    assert host.sysctl("net.ipv4.tcp_mem") == "56623104\t56623104\t56623104"
