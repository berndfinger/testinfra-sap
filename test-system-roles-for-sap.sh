#!/bin/bash
# test-system-roles-for-sap.sh: Test RHEL System Roles for SAP
# Author: Bernd Finger, Red Hat
# Tue Sep 24 15:57:45 CEST 2019
# license: Apache 2
# requires:
# testinfra (install using "pip install testinfra")
# testinfra license: Apache 2 - see https://github.com/philpep/testinfra/blob/master/README.rst

_NAME=$0

usage() { 
   echo "${_NAME}: Test RHEL System Roles for SAP"
   echo ""
   echo "test-system-roles-for-sap-sh <role> <host>"
   echo "  <role>: name of role: sap-preconfigure , sap-netweaver-preconfigure , or sap-hana-preconfigure"
   echo "  <host>: name of host to check"
   echo ""
   echo "Example:"
   echo "${_NAME} sap-preconfigure localhost"
}

if [[ $# -ne 2 ]]; then
   usage
   exit 1
fi

_ROLE=$1
if [[ ${_ROLE}. = "." ]]; then
   echo "Please enter name of role to test: sap-preconfigure , sap-netweaver-preconfigure , or sap-hana-preconfigure"
   read _ROLE
fi

_REMOTE_HOST=$2
if [[ ${_REMOTE_HOST}. = "." ]]; then
   echo "Please enter name of the remote host to check:"
   read _REMOTE_HOST
fi

_ARCH=$(ssh ${_REMOTE_HOST} uname -m)

_RHEL=$(ssh ${_REMOTE_HOST} cat /etc/redhat-release | awk 'BEGIN{FS="release "}{split ($2, a, "."); print a[1]}')
# alternative method: use the kernel version
# _KERNEL=$(ssh ${_REMOTE_HOST} uname -r | cut -d "." -f 1)
# case ${_KERNEL} in
#   3) _RHEL=7
#      ;;
#   4) _RHEL=8
#      ;;
#   *) echo "${_KERNEL} not supported. Exit."
#      exit 1
#      ;;
# esac

case ${_ROLE} in
   "sap-preconfigure")
      case ${_RHEL} in
         7) SAPNOTES="2002167 1391070"
            ;;
         8) SAPNOTES="2772999"
            ;;
         *) 
            echo "not supported. Exit."
            exit 1
            ;;
      esac
      ;;
   "sap-netweaver-preconfigure") SAPNOTES="2526952"
      ;;
   "sap-hana-preconfigure")
      case ${_RHEL} in
         7) SAPNOTES="2009879 2292690 2455582 2382421"
            if [[ ${_ARCH}. = "ppc64le". ]]; then
               SAPNOTES="${SAPNOTES} 2055470_7"
            fi
            ;;
         8) SAPNOTES="2772999 2777782 2382421"
            if [[ ${_ARCH}. = "ppc64le". ]]; then
               SAPNOTES="${SAPNOTES} 2055470_8"
            fi
            ;;
         *) 
            echo "not supported. Exit."
            exit 1
            ;;
      esac
      ;;
esac

echo _ROLE: ${_ROLE}
echo _REMOTE_HOST: ${_REMOTE_HOST}
echo _ARCH: ${_ARCH}
# echo _KERNEL: ${_KERNEL}
echo _RHEL: ${_RHEL}
echo SAPNOTES: ${SAPNOTES}

CURRENT_DIR=$(pwd)

# role-independent or RHEL-release-indenendent python include files are in:
export PYTHONPATH="${CURRENT_DIR}/sap-generic:${CURRENT_DIR}/${_ROLE}/generic"
echo PYTHONPATH=${PYTHONPATH}

for sapnote in ${SAPNOTES}; do
   for file in $(find ${_ROLE}/sapnote/${sapnote} -name "*.py" | sort -n); do
# alternative to PYTHONPATH: use cpp to include files, using: '#include "file.py"'
#      echo "file before cpp: ${file}"
#      _dir=$(dirname ${file})
#      _file=$(basename ${file})
#      cd ${_dir}
#      cpp_file=$(echo ${file} | awk '{gsub ("/", "_"); print}')
#      echo "files to include: $(awk '!/# /{print}' ${_file} | cpp -P -MM | awk '{$1=""; print}')"
#      awk '!/# /{print}' ${_file} | cpp -P > ${CURRENT_DIR}/${cpp_file}
#      cpp -P ${file} > ./${cpp_file}
#      cd ${CURRENT_DIR}
#      echo py.test --hosts=${_REMOTE_HOST} --connection=ssh -v ./${cpp_file}
#      py.test --hosts=${_REMOTE_HOST} --connection=ssh -v ./${cpp_file}
      echo py.test --hosts=${_REMOTE_HOST} --connection=ssh -v ./${file}
      py.test --hosts=${_REMOTE_HOST} --connection=ssh -v ./${file}
#      rm ./${cpp_file}
   done
done
