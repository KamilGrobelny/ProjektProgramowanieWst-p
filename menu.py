import FunkcjeZgadywanka as FZ
import os
import sys
nick1, nick2='', ''
if len(sys.argv)>1:
    nick1=sys.argv[1]
if len(sys.argv)>2:
    nick2=sys.argv[2]
if nick1=='':
    nick1="Gracz 1"
if nick2=='':
    nick2="Gracz 2"
dzialanie = True
while(dzialanie):
    menu_glowne=input("Wybierz opcje gry: \n 1 - zgadujesz szyfr wymyślony przez komputer \n 2 - komputer zgaduje szyfr wymyślony przez Ciebie \n 3 - grasz z drugim graczem \n 4 - zakończ program \n Wybór: ")
    if (menu_glowne=='1'):
        print("Tryb gry: gracz kontra komputer")
        FZ.PvC()
        break
    elif (menu_glowne=='2'):
        print("Tryb gry: komputer kontra gracz")
        while(True):
            menu_CvP=input("Wybierz opcje gry: \n 1 - komputer automatycznie otrzymuje informację zwrotną \n 2 - Gracz samodzielnie podaje informację zwrotną komputerowi \n 3 - Zmień tryb gry \n Wybór: ")
            if(menu_CvP=='1'):
                print("Tryb gry: komputer kontra gracz (komputer automatycznie otrzymuje informację zwrotną)")
                FZ.CvP(1)
                dzialanie=False
                break
            elif(menu_CvP=='2'):
                print("Tryb gry: komputer kontra gracz (gracz podaje komputerowi informację zwrotną)")
                FZ.CvP(2)
                dzialanie=False
                break
            elif(menu_CvP=='3'):
                break
            os.system('clear')
    elif (menu_glowne=='3'):
        dzialanie2=True
        while(dzialanie2):
            print("Wybrany tryb: gracz kontra gracz")
            menu_PvP = input("Wybierz opcje gry: \n 1 - komputer losuje szyfry dla graczy \n 2 - gracze wymyślają szyfry dla oponenta \n 3 - Zmień tryb gry \n Wybór: ")
            if(menu_PvP=='1'):
                print("Tryb gry: gracz kontra gracz (komputer losuje szyfry dla graczy)")
                FZ.PvP1(nick1, nick2)
                dzialanie=False
                break
            elif(menu_PvP=='2'):
                print("Tryb gry: gracz kontra gracz (gracze wymyślają szyfry dla oponenta)")
                while(True):
                    menu_PvP2 = input("Wybierz opcje gry: \n 1 - gracze automatycznie otrzymują informację zwrotną \n 2 - gracze podają wzajemnie informacje zwrotne \n 3 - Zmień tryb gry \n Wybór: ")
                    if(menu_PvP2=='1'):
                        print("Tryb gry: gracz kontra gracz (gracze wymyślają szyfry dla oponenta)(gracze automatycznie otrzymują informację zwrotną)")
                        FZ.PvP2(1, nick1, nick2)
                        dzialanie=False
                        dzialanie2=False
                        break
                    elif(menu_PvP2=='2'):
                        print("Tryb gry: gracz kontra gracz (gracze wymyślają szyfry dla oponenta)(gracze podają wzajemnie informacje zwrotne)")
                        FZ.PvP2(2, nick1, nick2)
                        dzialanie=False
                        dzialanie2=False
                        break
                    elif(menu_PvP2=='3'):
                        break
                break
            elif(menu_PvP=='3'):
                break
            os.system('clear')
    elif (menu_glowne=='4'):
        break 
    else:
        os.system('clear')