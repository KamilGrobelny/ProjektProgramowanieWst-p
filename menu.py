from random import randint
import funkcje as FZ

opcja=int(input("Wybierz opcje gry: \n 1 - zgadujesz szyfr wymyślony przez komputer \n 2 - komputer zgaduje szyfr wymyślony przez Ciebie \n 3 - grasz z drugim graczem \n"))
if (opcja==1):
    FZ.PvC()
if (opcja==2):
    print("czekamy na Janka")
if (opcja==3):
    opcja1 = int(input("Wybierz opcje gry: \n 1 - komputer losuje wam liczby \n 2 - sami wybieracie sobie liczby dla przecinika \n"))
    if (opcja1 == 1):
        FZ.PvP1()
    if (opcja1 == 2):
        FZ.PvP2()
