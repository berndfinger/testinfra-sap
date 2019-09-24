def test_tuned_profiles_sap_installed(host):
    tuned_profiles_sap = host.package("tuned-profiles-sap")
    assert tuned_profiles_sap.is_installed
    assert tuned_profiles_sap.version.startswith("2.1")

def test_tuned_is_installed(host):
    tuned = host.package("tuned")
    assert tuned.is_installed

def test_tuned_running_and_enabled(host):
    tuned = host.service("tuned")
    assert tuned.is_running
    assert tuned.is_enabled

def test_tuned_profiles_sap_netweaver_active(host):
    command = host.run("/usr/sbin/tuned-adm active | awk '{printf (\"%s|\", $NF)}'")
    assert command.stdout.startswith("sap-netweaver|")
