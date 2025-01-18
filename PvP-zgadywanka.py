from random import randint

def PoprawnoscProby(proba, n, zgadywana):
    """Funkcja sprawdza czy odgadnięcie podane przez użytkownika jest poprawnie wyrażone: odpowiednia długość n oraz same cyfry
    jeżeli dane nie są poprawnie  wyrażone to funkcja zwraca True"""
    if len(proba) > n:
        print("Podano za długi szyfr, spróbuj jeszcze raz")
        return True
    if len(proba) < n:
        print("Podano za krótki szyfr, spróbuj jeszcze raz")
        return True
    for i in proba:
        if ord(i) > 57 or ord(i) < 48:
            print("W szyfrze mogą być tylko cyfry, spróbuj jeszcze raz")
            return True


def InfoZwrotne(x, zgadywana, n):
    """Funkcja zwraca tablicę z wartościami cyfr na właściwych oraz niewłaściwych miejscach
    Tablica[0] to cyfry na właściwych miejscach
    Tablica[1] to cyfry na niewłaściwych miejscach
    Funkcja jest uniwersalna: można ją stosować do pvp, pvc, cvp"""
    if x == zgadywana:
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
            if x[k] == KopiaZgadywana[k]:
                wlasciwe += 1
                x[k] = "&"
                KopiaZgadywana[k] = "%"
        for k in range(len(x)):
            for l in range(n):
                if x[k] == "&":
                    break
                elif x[k] == KopiaZgadywana[l]:
                    niewlasciwe += 1
                    x[k] = "&"
                    KopiaZgadywana[l] = "%"
                    break
        Tablica = [wlasciwe, niewlasciwe]
        return Tablica


def Odgadywanie(zgadywana, n, b):
    """Funkcja pobiera od użytkownika próbę. Za pomocą funkcji InfoZwrotne(x, zgadywana, n)
    sprawdza czy próba == szyfr, a jeśli nie to zwraca informację ile cyfr jest na właściwych i niewłaściwych miejscach"""
    proba = str(input("zgaduj: "))
    x = list(str(proba))
    if PoprawnoscProby(x, n, zgadywana):
        return Odgadywanie(zgadywana, n, b)
    b+=1
    for i in range(len(x)):
        x[i] = int(x[i])
    Wartosci = InfoZwrotne(x, zgadywana, n)
    if Wartosci[0] == n:
        return b
    else:
        print(f"na właściwych miejscach: {Wartosci[0]}")
        print(f"na niewłaściwych miejscach: {Wartosci[1]}")
        return Odgadywanie(zgadywana, n, b)


# Player vs Player - zmieniłem funkcje Odgadywanie -ilosckrokow(a), if Wartosci[0] == n: ...
n = int(input("podaj n: "))
a=0
if (n > 10) or (n < 1):
    raise ValueError("n musi być liczbą całowitą z przedziału [1, 10]")
zgadywana = []
zgadywana1 = []
for i in range(n):
    zgadywana.append(randint(0, 9))
b=Odgadywanie(zgadywana, n, a)
print("ZMIANA ZAWODNIKA.")
for i in range(n):
    zgadywana1.append(randint(0, 9))
c=Odgadywanie(zgadywana1, n, a)
if (b<c):
    print("Wygrał 1 zawodnik.")
elif (b==c):
    print("Remis")
else:
    print("Wygrał 2 zawodnik.")