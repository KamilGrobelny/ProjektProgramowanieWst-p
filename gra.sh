#!/bin/bash
#nazwy graczy podawane podczas uruchomiania gry
nick1=$1
nick2=$2
source .venv/Scripts/activate
which python
py menu.py $nick1 $nick2
deactivate