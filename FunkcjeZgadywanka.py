from random import randint
import os

def PoprawnoscN(n: str):
    """
    Funkcja sprawdza, czy wprowadzona przez użytkownika próba jest poprawnie wyrażona:
    - Czy długość próby jest zgodna z oczekiwaną.
    - Czy próba zawiera tylko cyfry.

    Parametry:
    @ n: Ciąg znaków reprezentujący oczekiwaną długość szyfru. Musi być liczbą całkowitą mieszczącą się w przedziale [1, 10].

    Zwraca:
    @ True: Jeśli próba jest niepoprawna (zawiera coś innego niż liczby lub liczba jest poza zakresem).
    @ False: Jeśli dane są poprawne (długość jest liczbą całkowitą w przedziale [1, 10]).

    Przykłady:
    >>> PoprawnoscN("abcd")
    "n musi być liczbą całkowitą, podaj n ponownie"  
    
    >>> PoprawnoscN("28")
    "n musi być liczbą całowitą z przedziału [1, 10], podaj n ponownie"  
    
    >>> PoprawnoscN("5")
    False  # poprawna próba :)
    """
    for i in range(len(n)):
        if ord(n[i])>57 or ord(n[i]) < 48:
            print("n musi być liczbą całkowitą, podaj n ponownie")
            return True
    n=int(n)
    if (n > 10) or (n < 1):
        print("n musi być liczbą całowitą z przedziału [1, 10], podaj n ponownie")
        return True

def PoprawnoscProby(proba: list, n: int):
    """Funkcja sprawdza, czy odgadnięcie podane przez użytkownika jest poprawnie wyrażone: czy ma odpowiednią długość 
    oraz czy zawiera tylko cyfry. Jeśli dane nie są poprawne, funkcja zwraca True, sygnalizując błąd.

    Funkcja sprawdza, czy długość próby jest zgodna z oczekiwaną długością szyfru (n) oraz czy wszystkie elementy w próbie 
    to cyfry. Jeśli którakolwiek z tych dwoch rzeczy jest niezgodna, funkcja zwraca komunikat o błędzie.

    Parametry:
    @ proba: Lista, która zawiera odgadnięcie użytkownika, przedstawioną jako listę cyfr (każdy element typu int).
                     Długość tej listy powinna odpowiadać długości szyfru (n).
    @ n: Długość szyfru, która musi zawierać się w przedziale [1, 10]. Określa, ile cyfr powinna zawierać próba.

    Przykład:
    >>> PoprawnoscProby([1, 2, 3], 3)
    True  # Długość próby jest odpowiednia, zawiera tylko cyfry.
    
    >>> PoprawnoscProby([1, 2, 'a'], 3)
    "W szyfrze mogą być tylko cyfry, spróbuj jeszcze raz".

    >>> PoprawnoscProby([1, 2], 3)
    "Podano za krótki szyfr, spróbuj jeszcze raz".

    >>> PoprawnoscProby([1, 2, 3, 4], 3)
    "Podano za długi szyfr, spróbuj jeszcze raz".
    """
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
    """Funkcja zwraca listę z wartościami cyfr na właściwych oraz niewłaściwych miejscach.
    
    Lista[0] zawiera liczbę cyfr na właściwych miejscach.
    Lista[1] zawiera liczbę cyfr na niewłaściwych miejscach.
    
    Parametry:
    @ x: Lista zawierająca odgadnięcia podane przez drugiego gracza. Musi być listą pojedynczych cyfr o typie int.
    @ zgadywana: Lista reprezentująca szyfr, który należy odgadnąć, podawany przez pierwszego gracza.
    @ n: Długość szyfru, która musi zawierać się w przedziale [1, 10].
    
    Przykład:
    >>> InfoZwrotne([1, 2, 3], [1, 4, 3], 3)
    [2, 0]
    
    Tutaj dwie cyfry (1 i 3) są na właściwych miejscach, a żadna cyfra nie znajduje się na niewłaściwym miejscu.
    
    Jeśli 'x' jest równe 'zgadywana', zwróci '[n, 0]', gdzie 'n' to długość szyfru, ponieważ wszystkie cyfry są na właściwych miejscach.
    """
    if x==zgadywana:
        wlasciwe = n
        niewlasciwe = 0
        return [wlasciwe, niewlasciwe]
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
        return [wlasciwe, niewlasciwe]
              
def Odgadywanie(zgadywana: list, n: int, krok: int):
    """Funkcja umożliwia odgadywanie szyfru przez użytkownika. Zwraca listę: [liczba kroków, True], 
    gdzie liczba kroków to liczba prób, które użytkownik podjął, a True oznacza, że udało się odgadnąć szyfr.

    Funkcja pobiera próbę od użytkownika, a następnie za pomocą funkcji InfoZwrotne(x: list, zgadywana: list, n: int) 
    sprawdza, ile cyfr jest na właściwych miejscach. Jeśli liczba cyfr na właściwych miejscach jest równa długości szyfru 'n', 
    użytkownik wygrał, a funkcja zwróci liczbę prób i wartość 'True'. Jeśli nie, użytkownik otrzyma informację, ile cyfr 
    jest na właściwych miejscach i ile na niewłaściwych, a następnie może spróbować ponownie.

    Parametry:
    @ zgadywana: Lista reprezentująca szyfr, który należy odgadnąć. Jest to lista cyfr o długości 'n'.
    @ n: Długość szyfru, która musi zawierać się w przedziale [1, 10].
    @ krok: Liczba dotychczasowych prób, zaczyna się od 0, a po każdej próbie zwiększa się o 1.

    Przykład:
    >>> Odgadywanie([1, 4, 3], 3, 0)
    Podaj swoje odgadnięcie: 143
    Liczba cyfr występujących w szyfrze na właściwych miejscach: 3
    wygrałeś, Twoja liczba odgadnięć: 1
    [1, True]
    """
    proba = str(input("Podaj swoje odgadnięcie: "))
    x = list(str(proba))
    if PoprawnoscProby(x, n):
        return Odgadywanie(zgadywana, n, krok)
    for i in range(len(x)):
        x[i]=int(x[i])
    Wartosci = InfoZwrotne(x, zgadywana, n)
    krok+=1
    if Wartosci[0]==n:
        print(f"Odgadłeś szyfr! Twoja liczba odgadnięć: {krok}")
        return [krok, True]
    else:
        print(f"Liczba cyfr występujących w szyfrze na właściwych miejscach: {Wartosci[0]}")
        print(f"Liczba cyfr występujących w szyfrze, ale które nie są na właściwych miejscach: {Wartosci[1]}")
        return Odgadywanie(zgadywana, n, krok)

def PvC():
    """Funkcja umożliwia grę człowieka z komputerem, gdzie człowiek zgaduje szyfr komputera.
    
    Gra przebiega w następujący sposób:
    1. Użytkownik podaje długość szyfru 'n' (gdzie 'n' musi być liczbą całkowitą z przedziału [1, 10]).
    2. Komputer generuje losowy szyfr o długości 'n'.
    3. Użytkownik zgaduje szyfr, wprowadzając swoje propozycje.
    4. Program sprawdza, ile cyfr zostało odgadniętych na właściwych miejscach.
    5. Gra kończy się, gdy użytkownik poprawnie odgadnie cały szyfr lub w przypadku innej zakończonej decyzji.
    
    Zwraca:
    @ 0: Zwraca wartość 0, jeśli użytkownik odgadł szyfr komputera.

    Przykład:
    >>> PvC()
    "Podaj n: "
    # Następnie użytkownik podaje długość szyfru, np. 4.
    # Komputer generuje szyfr, a użytkownik zgaduje itd.
    """
    n = input("podaj n: ")
    if n=="":
        return PvC()
    if PoprawnoscN(n):
        return PvC()
    n=int(n)
    zgadywana = []
    for i in range (n):
        zgadywana.append(randint(0, 9))
    if Odgadywanie(zgadywana, n, 0)[1]:
        return 0

def PvP1 ():
    """Funkcja umożliwia grę dwóch graczy (ludzi), gdzie komputer generuje szyfry dla obu graczy.
    
    Gra przebiega w następujący sposób:
    1. Użytkownicy podają długość szyfru 'n' (gdzie 'n' musi być liczbą całkowitą z przedziału [1, 10]). (długość obowiązuje obydwu graczy)
    2. Komputer losowo generuje szyfr dla obu graczy.
    3. Pierwszy gracz zgaduje szyfr drugiego gracza, a następnie drugi gracz zgaduje szyfr pierwszego.
    4. Funkcja porównuje liczbę prób potrzebnych do odgadnięcia szyfru przez obu graczy.
    5. Wynik gry jest ogłaszany: któryś gracz wygral, czy był remis.

    Przykład:
    >>> PvP1()
    "Podaj n: "
    # Następnie użytkownicy podają długość szyfru, np. 4.
    # Komputer generuje szyfry dla obu graczy, a następnie gracze próbują zgadnąć szyfr przeciwnika.
    # Po kilku próbach wynik gry jest ogłoszony (kto wygrał lub czy był remis).
    
    """
    n = input("podaj n: ")
    if n=="":
        return PvP1()
    a = 0
    if PoprawnoscN(n):
        return PvP1()
    n=int(n)
    zgadywana = []
    zgadywana1 = []
    for i in range(n):
        zgadywana.append(randint(0, 9))
    b = Odgadywanie(zgadywana, n, a)[0]
    print("ZMIANA ZAWODNIKA.")
    for i in range(n):
        zgadywana1.append(randint(0, 9))
    c = Odgadywanie(zgadywana1, n, a)[0]
    if (b < c):
        print("Wygrał 1 zawodnik.")
    elif (b == c):
        print("Remis")
    else:
        print("Wygrał 2 zawodnik.")

def PvP2 ():
    """Funkcja umożliwia grę dwóch graczy (człowiek vs człowiek), w której obaj gracze podają swoje szyfry, a następnie próbują je odgadnąć.
    
    Gra przebiega w następujący sposób:
    1. Gracze podają długość szyfru 'n' (gdzie 'n' musi być liczbą całkowitą z przedziału [1, 10]). (długość obowiązuje obydwu graczy)
    2. Drugi zawodnik podaje swój szyfr (n-cyfrowy), który będzie zgadywany przez pierwszego zawodnika.
    3. Funkcja wywołuje grę, w której pierwszy zawodnik próbuje zgadnąć szyfr drugiego zawodnika, a drugi zawodnik próbuje zgadnąć szyfr pierwszego.
    4. Po każdej próbie system sprawdza, ile cyfr zostało odgadniętych na właściwych miejscach.
    5. Wynik gry jest ogłaszany, który zawodnik wygrał lub czy jest remis.

    Przykład:
    >>> PvP2()
    "Podaj n: "
    # Gracze podają długość szyfru, np. 4.
    # Drugi zawodnik podaje swój szyfr, a potem pierwszy zawodnik zgaduje.
    # Po kilku próbach wynik gry jest ogłoszony (kto wygrał lub czy był remis). 
    """
    n = input("podaj n: ")
    if n=="":
        return PvP2()
    if PoprawnoscN(n):
        return PvP2()
    n=int(n)

    def PvP2_1():
        zgadywana = []
        x=input(f"Podaj liczbe {n}-cyfrową (zawodnik 2), która bedzie zgadywana przez przeciwnika (zawodnika 1): ")
        os.system('clear')
        if PoprawnoscProby(x, n):
            return PvP2_1()
        zgadywana=list(str(x))
        for i in range(len(zgadywana)):
            zgadywana[i]=int(zgadywana[i])
        return Odgadywanie(zgadywana, n, 0)[0]
    b = PvP2_1()

    def PvP2_2():
        zgadywana1=[]
        x = input(f"Podaj liczbe {n}-cyfrową (zawodnik 1), która bedzie zgadywana przez przeciwnika (zawodnik 2): ")
        os.system('clear')
        if PoprawnoscProby(x, n):
            return PvP2_2()
        zgadywana1=list(str(x))
        for i in range(len(zgadywana1)):
            zgadywana1[i]=int(zgadywana1[i])
        return Odgadywanie(zgadywana1, n, 0)[0]
    c = PvP2_2()

    if (b < c):
        print("Wygrał 1 zawodnik.")
    elif (b == c):
        print("Remis")
    else:
        print("Wygrał 2 zawodnik.")