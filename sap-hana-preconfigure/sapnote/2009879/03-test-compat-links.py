def test_link_libssl(host):
    command = host.run("ls -l /usr/lib64/libssl.so.1.0.1 | awk '/libssl.so.1.0.1 ->/{printf (\"%s|\", $NF)}'")
    assert command.stdout.startswith("/usr/lib64/libssl.so.10|")

def test_link_libcrypto(host):
    command = host.run("ls -l /usr/lib64/libcrypto.so.1.0.1 | awk '/libcrypto.so.1.0.1 ->/{printf (\"%s|\", $NF)}'")
    assert command.stdout.startswith("/usr/lib64/libcrypto.so.10|")
