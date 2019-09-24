def test_base_is_installed(host):
    command = host.run("yum group list -v server-product-environment | awk '/Installed Environment Groups:/{a=-99}{a++; if (a==-97){print $NF}}'")
    assert command.stdout.startswith("(server-product-environment)")

def test_packages_are_installed(host):
    assert host.package("uuidd").is_installed
    assert host.package("libnsl").is_installed
    assert host.package("tcsh").is_installed
    assert host.package("psmisc").is_installed

