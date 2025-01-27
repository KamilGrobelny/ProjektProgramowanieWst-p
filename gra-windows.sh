#!/bin/bash
#nazwy graczy podawane podczas uruchomiania gry
nick1=$1
nick2=$2
Katalog_Projektu=$(basename "$PWD")
source .venv/Scripts/activate
sciezka=$(which python)
if [[ "$sciezka" == *"/$Katalog_Projektu/.venv/"* ]]; then
    py menu.py $nick1 $nick2
    deactivate
else
    echo "Środowisko wirtualne nie zostało uruchomione"
fi