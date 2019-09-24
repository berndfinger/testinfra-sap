def test_tmpfs(host):
# size of /dev/shm not checked
    assert host.file("/etc/fstab").contains("/dev/shm")
    assert host.run_test("df -k /dev/shm")
