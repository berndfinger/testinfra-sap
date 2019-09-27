def test_rhel_eus_e4s_repos(host):
    command_result = host.run("yum repolist | awk '/^[!]rhel-7-server-e[4u]s-rpms/{a++}END{print a}'")
    assert int(command_result.stdout) >= 1

def test_rhel_sap_hana_eus_e4s_repos(host):
    command_result = host.run("yum repolist | awk '/^[!]rhel-sap-hana-for-rhel-7-server-e[4u]s-rpms/{a++}END{print a}'")
    assert int(command_result.stdout) >= 1
