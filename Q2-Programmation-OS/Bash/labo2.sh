#!/bin/bash

robertcount=0
testcount=0
rootcount=0
unknownarg=0

if [[  $# -eq 0 ]]; then
    echo -e 'Le script requiert au moins un arguments. Exiting.'
    exit 1
fi

echo "Nombre de paramètre(s): $#"

for arg in $@; do
    case $arg in
        robert)
            echo "Bonjour Robert"
            robertcount+=1
            ;;
        test)
            echo "Ceci est un compte test"
            testcount+=1
            ;;
        root)
            echo "Bienvenu cher administrateur"
            rootcount+=1
            ;;
        *)
            echo "$arg est inconnu"
            unknownarg+=1
            ;;
    esac
done

echo "Nombre de robert : $robertcount"
echo "Nombre de test : $testcount"
echo "Nombre d'administrateur : $rootcount"

if [[ $unknownarg -gt 0 ]]; then
    echo -e 'Le script contient un argument inconnu!'
    exit 1
fi

exit 0
