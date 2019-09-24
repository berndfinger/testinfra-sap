def test_hostnames(host):
# ip address check not implemented
    hostname_s = host.run("hostname -s").stdout.strip('\n')
    hostname_d = host.run("hostname -d").stdout.strip('\n')
    hostname_f = host.run("hostname -f").stdout.strip('\n')
    assert hostname_d != ""
    assert hostname_f == hostname_s + "." + hostname_d
    _host = host.addr (hostname_f)
    assert host.file("/etc/hosts").exists
    assert host.file("/etc/hosts").contains(hostname_f)
