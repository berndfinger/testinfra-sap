# def test_base_is_installed(host):
#    command = host.run("yum group list -v server-product-environment | awk '/Installed Environment Groups:/{a=-99}{a++; if (a==-97){print $NF}}'")
#    assert command.stdout.startswith("(server-product-environment)")

def test_packages_are_installed(host):
    assert host.package("chrony").is_installed
    assert host.package("xfsprogs").is_installed		
    assert host.package("libaio").is_installed 		
    assert host.package("net-tools").is_installed	
    assert host.package("bind-utils").is_installed	
    assert host.package("gtk2").is_installed		
    assert host.package("libicu").is_installed 		
    assert host.package("xulrunner").is_installed	
    assert host.package("tcsh").is_installed		
    assert host.package("sudo").is_installed		
    assert host.package("libssh2").is_installed		
    assert host.package("expect").is_installed 		
    assert host.package("cairo").is_installed		
    assert host.package("graphviz").is_installed		
    assert host.package("iptraf-ng").is_installed	
    assert host.package("krb5-workstation").is_installed	
    assert host.package("krb5-libs").is_installed	
    assert host.package("libpng12").is_installed		
    assert host.package("nfs-utils").is_installed	
    assert host.package("lm_sensors").is_installed	
    assert host.package("rsyslog").is_installed		
    assert host.package("openssl").is_installed		
    assert host.package("PackageKit-gtk3-module").is_installed 
    assert host.package("libcanberra-gtk2").is_installed	
    assert host.package("libtool-ltdl").is_installed	
    assert host.package("xorg-x11-xauth").is_installed 	
    assert host.package("numactl").is_installed		
    assert host.package("tuned").is_installed		
    assert host.package("tuned-profiles-sap-hana").is_installed
    assert host.package("compat-sap-c++-5").is_installed	
    assert host.package("compat-sap-c++-6").is_installed	
    assert host.package("compat-sap-c++-7").is_installed	
    assert host.package("libatomic").is_installed
