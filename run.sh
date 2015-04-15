#! /bin/bash

if [[ $# -ne 3 ]] ; then
    echo 'Usage:'
    echo './run.sh INTEGRATED-DATASET.csv min-supp min-conf'
    exit 0
fi

python main.py ${1} ${2} ${3}