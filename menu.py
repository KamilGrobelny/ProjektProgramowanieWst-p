from random import randint
import FunkcjeZgadywanka as FZ

while(True):
    opcja=int(input("Wybierz opcje gry: \n 1 - zgadujesz szyfr wymyślony przez komputer \n 2 - komputer zgaduje szyfr wymyślony przez Ciebie \n 3 - grasz z drugim graczem \n"))
    if (opcja==1):
        FZ.PvC()
        break
    if (opcja==2):
        print("czekamy na Janka")
        break
    if (opcja==3):
        while(True):
            opcja1 = int(input("Wybierz opcje gry: \n 1 - komputer losuje wam liczby \n 2 - sami wybieracie sobie liczby dla przecinika \n"))
            if (opcja1 == 1):
                FZ.PvP1()
                break
            if (opcja1 == 2):
                FZ.PvP2()
                break
            else:
                print("Wybierz 1 lub 2.")
    else:
        print("Wybierz 1, 2 lub 3.")
