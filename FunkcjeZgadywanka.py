from random import randint
def PoprawnoscProby(proba: list, n: int):
    """Funkcja sprawdza czy odgadnięcie podane przez użytkownika jest poprawnie wyrażone: odpowiednia długość n oraz same cyfry jeżeli dane nie są poprawnie  wyrażone to funkcja zwraca True
    @ proba: odgadnięcie podane przez drugiego gracza, musi być listą pojedynczych cyfr o typie int
    @ n: długość szyfru, która musi zawierać się w przedziale [1, 10]"""
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
    """Funkcja zwraca listę z wartościami cyfr na właściwych oraz niewłaściwych miejscach
    Lista[0] to cyfry na właściwych miejscach
    Lista[1] to cyfry na niewłaściwych miejscach
    Funkcja jest uniwersalna: można ją stosować do pvp, pvc, cvp
    @ x: odgadnięcie podane przez drugiego gracza, musi być listą pojedynczych cyfr o typie int
    @ zgadywana: szyfr, który trzeba odgadnąć, podawany na początku gry przez pierwszego gracza
    @ n: długość szyfru, która musi zawierać się w przedziale [1, 10]"""
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
              
def Odgadywanie(zgadywana: list, n: int, krok: int):
    """Funkcja zwraca listę: [liczba kroków, true]. Funkcja pobiera od użytkownika próbę. Za pomocą funkcji InfoZwrotne(x: list, zgadywana: list, n:list)
    sprawdza czy liczba cyfr na właściwych miejscach jest równa n, a jeśli nie to zwraca informację ile cyfr jest na właściwych i niewłaściwych miejscach
    @ zgadywana: szyfr, który trzeba odgadnąć, podawany na początku gry przez pierwszego gracza
    @ n: długość szyfru, która musi zawierać się w przedziale [1, 10]
    @ krok: domyślnie (na początku gry, czyli przy pierwszym wywołaniu) jest równy 0, krok zwiększa się o 1 po wywołaniu funkcji InfoZwrotne"""
    proba = str(input("Podaj swoje odgadnięcie: "))
    x = list(str(proba))
    if PoprawnoscProby(x, n):
        return Odgadywanie(zgadywana, n, krok)
    for i in range(len(x)):
        x[i]=int(x[i])
    Wartosci = InfoZwrotne(x, zgadywana, n)
    krok+=1
    if Wartosci[0]==n:
        print(f"wygrałeś, Twoja liczba odgadnięć: {krok}")
        return [krok, True]
    else:
        print(f"Liczba cyfr występujących w szyfrze na właściwych miejscach: {Wartosci[0]}")
        print(f"Liczba cyfr występujących w szyfrze, ale które nie są na właściwych miejscach: {Wartosci[1]}")
        return Odgadywanie(zgadywana, n, krok)

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
    for i in range (n):
        zgadywana.append(randint(0, 9))
    if Odgadywanie(zgadywana, n, 0)[1]:
        return 0