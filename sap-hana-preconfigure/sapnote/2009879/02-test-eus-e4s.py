def test_rhel_eus_e4s_repos(host):
    command_result = host.run("yum repolist | awk '/^[!]rhel-7-server-e[4u]s-rpms/{a++}END{print a}'")
    assert int(command_result.stdout) >= 1
# yum repolist rhel-sap-hana-for-rhel-7-server-eus-rpms
# yum repolist rhel-sap-for-rhel-7-server-eus-rpms
# yum repolist rhel-7-server-eus-rpms
# yum repolist rhel-7-server-e4s-rpms

#    assert (host.package("rhel-7-server-eus-rpms").is_installed or host.package("rhel-7-server-e4s-rpms").is_installed)

#def test_rhel_sap_hana_eus_e4s_is_installed(host):
#    assert = host.run("yum repolist | awk '/^[!]rhel-sap-7-server-e[4u]s-rpms/{a++;print}END{print a}'").stdout >= 1
#    assert (host.package("rhel-sap-hana-for-rhel-7-server-eus-rpms").is_installed or host.package("rhel-sap-hana-for-rhel-7-server-e4s-rpms").is_installed)
