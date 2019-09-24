# def test_base_is_installed(host):
#    command = host.run("yum grouplist -v | awk '/infrastructure-server-environment/{a=1}END{if (a==1){print \"installed\"}else{print \"absent\"}}'")
#    assert command.stdout.startswith("installed")

#     _large_systems = host.package("@large-systems")
#     _nfs_client = host.package("@network-file-system-client")
#     _compat_libraries = host.package("@compat-libraries")
#     _performance = host.package("@performance")

def test_packages_are_installed(host):
    assert host.package("uuidd").is_installed
    assert host.package("tcsh").is_installed
    assert host.package("psmisc").is_installed
