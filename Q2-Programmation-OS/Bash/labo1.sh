#!/bin/bash

interne="Programmation"

[ -z "${publique+x}" ] && echo "La variable publique n'est pas affeectée. Exiting." >&2 && exit 1

if [ -n "$publique" ]; then
    echo "${interne}${publique}"
else
    echo "La variable publique est vide" >&2
    exit 2
fi

exit 0
