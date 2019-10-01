# testinfra-sap
These testinfra scripts test if the most important SAP notes are applied to a RHEL 7 or RHEL 8 system. These scripts can also be used to verify the system status after the roles
- [sap-preconfigure](https://github.com/linux-system-roles/sap-preconfigure)
- [sap-netweaver-preconfigure](https://github.com/linux-system-roles/sap-netweaver-preconfigure)
- [sap-hana-preconfigure](https://github.com/linux-system-roles/sap-hana-preconfigure)

have been applied.

Usage: 
```
# ./test-system-roles-for-sap-sh <role> <host>
  <role>: name of role: sap-preconfigure , sap-netweaver-preconfigure , or sap-hana-preconfigure
  <host>: name of host to check
```

Example:
./test-system-roles-for-sap.sh sap-preconfigure localhost

SAP Notes coverage: See output of `find . -name sapnote -exec ls -1 {} \; | sort | uniq`:
- 1391070
- 2002167
- 2009879
- 2292690
- 2382421
- 2455582
- 2526952
- 2772999
- 2777782

Not yet fully implemented:
- checks for ppc64le
- checks for package groups
- checks for kernel and package versions
