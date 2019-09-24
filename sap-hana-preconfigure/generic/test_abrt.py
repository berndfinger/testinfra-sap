def test_abrt_uninstalled_or_stopped_and_disabled(host):
    abrt = host.package("abrt")
    if abrt.is_installed:
        abrtd_service = host.service("abrtd")
        assert not abrtd_service.is_running
        assert not abrtd_service.is_enabled

def test_abrt_ccpp_uninstalled_or_stopped_and_disabled(host):
    abrt_ccpp = host.package("abrt-addon-ccpp")
    if abrt_ccpp.is_installed:
        abrt_ccpp_service = host.service("abrt-ccpp")
        assert not abrt_ccpp_service.is_running
        assert not abrt_ccpp_service.is_enabled
