def test_packages_are_installed(host):
   assert host.package("librtas").is_installed
   assert host.package("ncurses-libs").is_installed
   assert host.package("readline").is_installed
   assert host.package("sqlite").is_installed
   assert host.package("sg3_utils").is_installed
   assert host.package("libgcc").is_installed
   assert host.package("libstdc++").is_installed
   assert host.package("zlib").is_installed
   assert host.package("iprutils").is_installed
   assert host.package("lsvpd").is_installed
   assert host.package("libvpd").is_installed
   assert host.package("libservicelog").is_installed
   assert host.package("servicelog").is_installed
   assert host.package("ppc64-diag").is_installed

def test_packages_are_not_installed(host):
   assert not host.package("pseries-energy").is_installed
