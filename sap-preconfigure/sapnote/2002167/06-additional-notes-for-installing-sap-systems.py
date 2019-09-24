def test_link_libldap(host):
    command = host.run("ls -l /usr/lib64/libldap.so.199 | awk '/libldap.so.199 ->/{printf (\"%s|\", $NF)}'")
    assert command.stdout.startswith("/usr/lib64/libldap-2.3.so.0|")

def test_link_liblber(host):
    command = host.run("ls -l /usr/lib64/liblber.so.199 | awk '/liblber.so.199 ->/{printf (\"%s|\", $NF)}'")
    assert command.stdout.startswith("/usr/lib64/liblber-2.3.so.0|")

from test_systemd_tmpfiles import *
