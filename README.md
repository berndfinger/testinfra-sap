# testinfra-sap
These testinfra scripts test if the most important SAP notes are applied to a RHEL 7 or RHEL 8 system.

Usage: 
# ./test-system-roles-for-sap.sh
./test-system-roles-for-sap.sh: Test RHEL System Roles for SAP

test-system-roles-for-sap-sh <role> <host>
  <role>: name of role: sap-preconfigure , sap-netweaver-preconfigure , or sap-hana-preconfigure
  <host>: name of host to check

Example:
./test-system-roles-for-sap.sh sap-preconfigure localhost
