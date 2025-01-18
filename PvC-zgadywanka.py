#Player vs computer, tylko czlowiek zgaduje
"""
v1.0.1
"""
from random import randint
def PoprawnoscProby(proba: list, n: int, zgadywana: list):
    """Funkcja sprawdza czy odgadnięcie podane przez użytkownika jest poprawnie wyrażone: odpowiednia długość n oraz same cyfry
    jeżeli dane nie są poprawnie  wyrażone to funkcja zwraca True"""
    if len(proba) > n:
        print("Podano za długi szyfr, spróbuj jeszcze raz")
        return True
    if len(proba) < n:
        print("Podano za krótki szyfr, spróbuj jeszcze raz")
        return True
    for i in proba:
        if ord(i)>57 or ord(i) < 48:
            print("W szyfrze mogą być tylko cyfry, spróbuj jeszcze raz")
            return True

def InfoZwrotne(x: list, zgadywana: list, n: int):
    """Funkcja zwraca tablicę z wartościami cyfr na właściwych oraz niewłaściwych miejscach
    Tablica[0] to cyfry na właściwych miejscach
    Tablica[1] to cyfry na niewłaściwych miejscach
    Funkcja jest uniwersalna: można ją stosować do pvp, pvc, cvp"""
    if x==zgadywana:
        wlasciwe = n
        niewlasciwe = 0
        Tablica = [wlasciwe, niewlasciwe]
        return Tablica
    else:
        KopiaZgadywana = []
        for i in zgadywana:
            KopiaZgadywana.append(i)
        wlasciwe = 0
        niewlasciwe = 0
        for k in range(len(x)):
            if x[k]==KopiaZgadywana[k]:
                wlasciwe += 1
                x[k]="&"
                KopiaZgadywana[k]="%"
        for k in range(len(x)):
            for l in range(n):
                if x[k]=="&":
                    break
                elif x[k]==KopiaZgadywana[l]:
                    niewlasciwe += 1
                    x[k]="&"
                    KopiaZgadywana[l]="%"
                    break
        Tablica = [wlasciwe, niewlasciwe]
        return Tablica
              
def Odgadywanie(zgadywana: list, n: int):
    """Funkcja pobiera od użytkownika próbę. Za pomocą funkcji InfoZwrotne(x, zgadywana, n)
    sprawdza czy próba == szyfr, a jeśli nie to zwraca informację ile cyfr jest na właściwych i niewłaściwych miejscach"""
    proba = str(input("zgaduj: "))
    x = list(str(proba))
    if PoprawnoscProby(x, n, zgadywana):
        return Odgadywanie(zgadywana, n)
    for i in range(len(x)):
        x[i]=int(x[i])
    Wartosci = InfoZwrotne(x, zgadywana, n)
    if Wartosci[0]==n:
        return True
    else:
        print(f"na właściwych miejscach: {Wartosci[0]}")
        print(f"na niewłaściwych miejscach: {Wartosci[1]}")
        return Odgadywanie(zgadywana, n)

def PvC():
    """Funkcja umożliwia grę człowieka z komputerem, człowiek zgaduje szyfr komputera"""
    n = input("podaj n: ")
    for i in range(len(n)):
        if ord(n[i])>57 or ord(n[i]) < 48:
            print("n musi być liczbą całkowitą, podaj n ponownie")
            return PvC()
    n=int(n)
    if (n > 10) or (n < 1):
        print("n musi być liczbą całowitą z przedziału [1, 10], podaj n ponownie")
        return PvC()
    zgadywana = []
    zgadywana.append(randint(0, 9))
    if Odgadywanie(zgadywana, n):
        print("wygrałeś")
        return 0
PvC()
#End