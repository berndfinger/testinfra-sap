def test_numad_uninstalled_or_stopped_and_disabled(host):
    numad = host.package("numad")
    if numad.is_installed:
        numad = host.service("numad")
        assert not numad.is_running
        assert not numad.is_enabled
