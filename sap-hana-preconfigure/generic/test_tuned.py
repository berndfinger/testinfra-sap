def test_tuned_profiles_sap_hana_2_1_installed(host):
    tuned_profiles_sap_hana = host.package("tuned-profiles-sap-hana")
    assert tuned_profiles_sap_hana.is_installed
    assert tuned_profiles_sap_hana.version.startswith("2.1")

def test_tuned_installed(host):
    tuned = host.package("tuned")
    assert tuned.is_installed

def test_tuned_running_and_enabled(host):
    tuned = host.service("tuned")
    assert tuned.is_running
    assert tuned.is_enabled

def test_tuned_profiles_sap_hana_active(host):
    command = host.run("/usr/sbin/tuned-adm active | awk '{printf (\"%s|\", $NF)}'")
    assert command.stdout.startswith("sap-hana|")

