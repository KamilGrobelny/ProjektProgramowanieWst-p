from random import randint
import os

def PoprawnoscInformacji(wartosc1: str, wartosc2: str, n: int):
    """
    Sprawdza, czy podane wartości informacji zwrotnej są zgodne z oczekiwaniami.

    Funkcja weryfikuje następujące warunki:
    1. 'wartosc1' i 'wartosc' zawierają wyłącznie cyfry.
    2. Żadne z podanych wartości nie są puste.
    3. Suma wartości 'wartosc1' i 'wartosc2' nie przekracza 'n'.

    Argumenty:
        @ wartosc1: Pierwsza wartość wejściowa (liczba cyfr na właściwych miejscach).
        @ wartosc2: Druga wartość wejściowa (liczba cyfr na niewłaściwych miejscach).
        @ n: Długość szyfru.

    Zwraca:
            -'True'-jeśli podane wartości są poprawne.
            -'False'-w przeciwnym wypadku, wypisuje odpowiedni komunikat błędu.

    Przykłady:
        >>> PoprawnoscInformacji(2, 1, 4)
        True
        
        >>> PoprawnoscInformacji(3, 2, 4)
        Suma podanych wartości nie może być większa od 4. Spróbuj ponownie.
        False
        
        >>> PoprawnoscInformacji(2a, 1, 4)
        Podana wartość musi zawierać tylko cyfry. Spróbuj ponownie.
        False
        
        >>> PoprawnoscInformacji(1, , 4)
        Nie podano co najmniej jednej wartości. Spróbuj ponownie.
        False
    """
        for i in range(len(wartosc1)):
            if ord(wartosc1[i])>57 or ord(wartosc1[i]) < 48:
                print(f"Podana wartość musi zawierać tylko cyfry. Spróbuj ponownie.")
                return False
        for i in range(len(wartosc2)):
            if ord(wartosc2[i])>57 or ord(wartosc2[i]) < 48:
                print(f"Podana wartość musi zawierać tylko cyfry. Spróbuj ponownie.")
                return False
        if wartosc1=='' or wartosc2=='':
            print("Nie podano co najmniej jednej wartości. Spróbuj ponownie")
            return False
        if (int(wartosc1)+int(wartosc2))>n:
            print(f"Suma podanych wartości nie może być większa od {n}. Spróbuj ponownie.")
            return False
        return True

def PoprawnoscN(n: str):
    """
    Funkcja sprawdza, czy wprowadzona przez użytkownika próba jest poprawnie wyrażona:
    - Czy długość próby jest zgodna z oczekiwaną.
    - Czy próba zawiera tylko cyfry.

    Parametry:
    @ n: Ciąg znaków reprezentujący oczekiwaną długość szyfru. Musi być liczbą całkowitą mieszczącą się w przedziale [1, 20].

    Zwraca:
    @ True: Jeśli próba jest niepoprawna (zawiera coś innego niż liczby lub liczba jest poza zakresem).
    @ False: Jeśli dane są poprawne (długość jest liczbą całkowitą w przedziale [1, 20]).

    Przykłady:
    >>> PoprawnoscN("abcd")
    "n musi być liczbą całkowitą, podaj n ponownie"  
    
    >>> PoprawnoscN("28")
    "n musi być liczbą całowitą z przedziału [1, 20], podaj n ponownie"  
    
    >>> PoprawnoscN("5")
    False  # poprawna próba :)
    """
    for i in range(len(n)):
        if ord(n[i])>57 or ord(n[i]) < 48:
            print("n musi być liczbą całkowitą, podaj n ponownie")
            return True
    n=int(n)
    if (n > 20) or (n < 1):
        print("n musi być liczbą całowitą z przedziału [1, 20], podaj n ponownie")
        return True

def PoprawnoscProby(proba: list[str], n: int):
    """Funkcja zwraca True jeżeli odgadnięcie nie jest poprawnie wyrażone oraz False jeżeli odgadnięcie zostało podane poprawnie.

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
    return False

def InfoZwrotne(x: list[int], zgadywana: list[int], n: int):
    """Funkcja zwraca listę z wartościami cyfr na właściwych oraz niewłaściwych miejscach.
    WAŻNE - po wywołaniu tej funkcji należy zwiększyć liczbę podjętych przez drugiego gracza prób o 1
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
              
def Odgadywanie(zgadywana: list[int], n: int, krok: int, Tryb_Gry: int, nazwa1: str, nazwa2: str):
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
    @ Tryb_Gry: 1 - gracz automatycznie otrzymuje informację zwrotną, 2 - gracz otrzymuje informację zwrotną od drugiego gracza (Tylko w trybie PvP2)
    @ nazwa1, nazwa2: nazwy graczy, nazwa1 to nazwa odgadującego, nazwa2 to nazwa gracza, którego szyfr należy odgadnąć.
    Przykład:
    >>> Odgadywanie([1, 4, 3], 3, 0, 1, nazwa1, nazwa2)
    Podaj swoje odgadnięcie: 143
    Liczba cyfr występujących w szyfrze na właściwych miejscach: 3
    {nazwa1} Odgadłeś szyfr! Twoja liczba odgadnięć: 1
    [1, True]
    """
    proba = str(input(f"{nazwa1} Podaj swoje odgadnięcie: "))
    x = list(str(proba))
    if PoprawnoscProby(x, n):
        return Odgadywanie(zgadywana, n, krok, Tryb_Gry, nazwa1, nazwa2)
    for i in range(len(x)):
        x[i]=int(x[i])
    if Tryb_Gry==1:
        Wartosci = InfoZwrotne(x, zgadywana, n)
    else:
        while(True):
            Wartosci=[input(f"{nazwa2} Podaj liczbę cyfr na właściwych miejscach: "), input(f"{nazwa2} Podaj liczbę cyfr na niewłaściwych miejscach: ")]
            if PoprawnoscInformacji(Wartosci[0], Wartosci[1], n):
                Wartosci[0]=int(Wartosci[0])
                Wartosci[1]=int(Wartosci[1])
                break
    krok+=1
    if Wartosci[0]==n:
        print(f"{nazwa1} Odgadłeś szyfr! Twoja liczba odgadnięć: {krok}")
        return [krok, True]
    else:
        if Tryb_Gry==1:
            print(f"Liczba cyfr występujących w szyfrze na właściwych miejscach: {Wartosci[0]}")
            print(f"Liczba cyfr występujących w szyfrze, ale które nie są na właściwych miejscach: {Wartosci[1]}")
            return Odgadywanie(zgadywana, n, krok, Tryb_Gry, nazwa1, nazwa2)
        else:
            return Odgadywanie(zgadywana, n, krok, Tryb_Gry, nazwa1, nazwa2)

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
    while(True):
        n = input("Podaj n [1, 20]: ")
        if not(n=="" or PoprawnoscN(n)):
            break
    n=int(n)
    zgadywana = []
    for i in range (n):
        zgadywana.append(randint(0, 9))
    if Odgadywanie(zgadywana, n, 0, 1, '', '')[1]:
        return 0

def PvP1 (nick1: str, nick2: str):
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
    # Komputer generuje szyfry dla obu graczy, a następnie gracze próbują zgadnąć szyfr.
    # Po kilku próbach wynik gry jest ogłoszony (kto wygrał lub czy był remis).
    
    """
    while(True):
        n = input("Podaj n [1, 20]: ")
        if not(n=="" or PoprawnoscN(n)):
            break
    n=int(n)
    zgadywana = []
    zgadywana1 = []
    for i in range(n):
        zgadywana.append(randint(0, 9))
    b = Odgadywanie(zgadywana, n, 0, 1, nick1, nick2)[0]
    print("ZMIANA ZAWODNIKA.")
    for i in range(n):
        zgadywana1.append(randint(0, 9))
    c = Odgadywanie(zgadywana1, n, 0, 1, nick2, nick1)[0]
    if (b < c):
        print(f"Wygrał {nick1}")
    elif (b == c):
        print("Remis")
    else:
        print(f"Wygrał {nick2}")

def PvP2 (Tryb_Gry: int, nick1: str, nick2: str):
    """Funkcja umożliwia grę dwóch graczy (człowiek vs człowiek), w której gracze wymyślają szyfry, a następnie próbują je wzajemnie odgadnąć.
    
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
    # Drugi zawodnik podaje swój szyfr, a potem pierwszy zawodnik zgaduje. Następnie następuje zamiana ról.
    # Po kilku próbach wynik gry jest ogłoszony (kto wygrał lub czy był remis). 
    """
    while(True):
        n = input("Podaj n [1, 20]: ")
        if not(n=="" or PoprawnoscN(n)):
            break
    n=int(n)

    def PvP2_1():
        zgadywana = []
        x=input(f"{nick2} Podaj liczbe {n}-cyfrową, która bedzie zgadywana przez przeciwnika {nick1}: ")
        os.system('clear')
        if PoprawnoscProby(x, n):
            return PvP2_1()
        zgadywana=list(str(x))
        for i in range(len(zgadywana)):
            zgadywana[i]=int(zgadywana[i])
        return Odgadywanie(zgadywana, n, 0, Tryb_Gry, nick1, nick2)[0]
    b = PvP2_1()

    def PvP2_2():
        zgadywana1=[]
        x = input(f"{nick1} Podaj liczbe {n}-cyfrową, która bedzie zgadywana przez przeciwnika {nick2}: ")
        os.system('clear')
        if PoprawnoscProby(x, n):
            return PvP2_2()
        zgadywana1=list(str(x))
        for i in range(len(zgadywana1)):
            zgadywana1[i]=int(zgadywana1[i])
        return Odgadywanie(zgadywana1, n, 0, Tryb_Gry, nick2, nick1)[0]
    c = PvP2_2()

    if (b < c):
        print(f"Wygrał {nick1}")
    elif (b == c):
        print("Remis")
    else:
        print(f"Wygrał {nick2}")
def CvP(Tryb_Gry: int):
   """
    Główna funkcja obsługująca tryb gry CvP-"Computer vs Player".
    Komputer próbuje odgadnąć szyfr podany przez użytkownika.

    Parametry:
        Tryb_Gry (int): Wybór trybu gry.
            @ Tryb 1: Komputer korzysta z funkcji InfoZwrotne, która automatycznie generuje informację zwrotną.
            @ Tryb 2: Użytkownik ręcznie podaje informację zwrotną, z możliwością kłamania.

    Funkcja:
        - Prosi użytkownika o długość szyfru 'n' (liczbę cyfr w szyfrze).
        - Wykorzystuje mechanizm zgadywania oparty na funkcjach 'szukanie_liczb` i `szukanie_miejsca`.
        - Wyświetla wynik oraz liczbę prób potrzebnych do odgadnięcia.
    """
    while(True):
        n = input("Podaj n [1, 20]: ")
        if not(n=="" or PoprawnoscN(n)):
            break
    n=int(n)
    
    def szukanie_liczb(zgadywana: list[int]):
        """
        Funkcja identyfikuje cyfry, które mogą być częścią szyfru, 
        na podstawie informacji zwrotnych podanych przez użytkownika lub funkcji InfoZwrotne.

        Argumenty:
                @ zgadywana: Lista cyfr reprezentująca szyfr, który komputer próbuje odgadnąć.

        Zwraca:
                @ mozliwe_cyfry: Lista cyfr, które są częścią szyfru.
                @ liczba_prob: Liczba prób, jakie wykonał komputer.
                @ zapychacz1: Lista składająca się z cyfry pełniącej rolę zapychacza oraz jej liczby wystąpień.
                @ zapychacz2: Jak wyżej, dla drugiej cyfry zapychacza.
        Przykład:
        >>> szukanie_liczb([2, 0, 3, 1])
        ([2, 0, 3, 1], 4, [7, 0], [8, 0])
        """
        ilosc_ruchow = 0
        zapychacz1 = [7, 0]
        zapychacz2 = [8, 0]
        mozliwe_liczby = []
        reszta = n
        dostepne_liczby = list(range(10))  
        for i in dostepne_liczby:
            if len(mozliwe_liczby)==n:
                return mozliwe_liczby, ilosc_ruchow, zapychacz1, zapychacz2
            elif i == 9:
                mozliwe_liczby.extend([9] * reszta)
                return mozliwe_liczby, ilosc_ruchow, zapychacz1, zapychacz2
            proba = [i] * n
            print("Próba:", "".join(map(str, proba)))
            if Tryb_Gry==1:
                tablica = InfoZwrotne(proba, zgadywana, n)
            else:
                while(True):
                    tablica=[input("Podaj liczbę cyfr na właściwych miejscach: "), input("Podaj liczbę cyfr na niewłaściwych miejscach: ")]
                    if PoprawnoscInformacji(tablica[0], tablica[1], n):
                        tablica[0]=int(tablica[0])
                        tablica[1]=int(tablica[1])
                        break
            ilosc_ruchow += 1
            if tablica[1] > 0:
                mozliwe_liczby.extend([i] * tablica[1])
                reszta-=tablica[1]
            if tablica[0] > 0:
                mozliwe_liczby.extend([i] * tablica[0])
                reszta-=tablica[0]
                if i==zapychacz1[0]:
                    zapychacz1[1]+=tablica[0]
                elif i==zapychacz2[0]:
                    zapychacz2[1]+=tablica[0]
        return mozliwe_liczby, ilosc_ruchow, zapychacz1, zapychacz2
    
    def szukanie_miejsca(haslo: list[int], mozliwe_liczby: list[int], zgadywana: list[int], ilosc_ruchow: int, zapychacz1: list[int], zapychacz2: list[int]):
    """
    Funkcja ustala miejsca dla poprawnych liczb w haśle.

    Wykorzystuje dostępne informacje o możliwych liczbach i ich poprawnych pozycjach,
    aby wypełnić hasło zgodnie z zasadami gry. Działa w trybie komputer vs gracz (Tryb_Gry == 1)
    lub w trybie, w którym użytkownik ręcznie podaje informacje zwrotne.

    Parametry:
        @ haslo: Aktualny stan hasła, w którym niektóre miejsca mogą być jeszcze nieznane.
        @ mozliwe_liczby: Lista liczb, które mogą występować w haśle.
        @ zgadywana: Szyfr, który komputer próbuje odgadnąć (w trybie automatycznym).
        @ ilosc_ruchow: Liczba wykonanych prób zgadywania.
        @ zapychacz1: Pierwsza liczba zapychająca i licznik jej wystąpień w haśle.
        @ zapychacz2: Druga liczba zapychająca i licznik jej wystąpień w haśle.

    Zwraca:
            -Finalny stan hasła po ustaleniu pozycji wszystkich liczb.
            -Łączną liczbę prób zgadywania.
            -Czy hasło zostało poprawnie odgadnięte.
    """
        miejsca = list(range(n))
        def funkcja_pomocnicza(haslo, zgadywana, n, ilosc_ruchow):
        """
        Funkcja pomocnicza sprawdzająca poprawność odgadnięcia hasła.

        Parametry:
            @ haslo: Aktualne hasło po kolejnych próbach.
            @ zgadywana: Szyfr, który komputer próbuje odgadnąć (w trybie automatycznym).
            @ n: Długość hasła.
            @ ilosc_ruchow: Liczba prób zgadywania.

        Przykłady:
            >>> funkcja_pomocnicza([2, 0, 3, 1], [2, 0, 3, 1], 4, 4)
            ([2, 0, 3, 1], 5, True)
        """
            ilosc_ruchow+=1
            if Tryb_Gry==1:
                if InfoZwrotne(haslo, zgadywana, n)[0]==n:
                    print("Próba:", "".join(map(str, haslo)))
                    return haslo, ilosc_ruchow, True
                else:
                    return haslo, ilosc_ruchow, False
            else:
                print("Próba:", "".join(map(str, haslo)))
                while(True):
                    tablica=[input("Podaj liczbę cyfr na właściwych miejscach: "), input("Podaj liczbę cyfr na niewłaściwych miejscach: ")]
                    if PoprawnoscInformacji(tablica[0], tablica[1], n):
                        tablica[0]=int(tablica[0])
                        tablica[1]=int(tablica[1])
                        break
                if tablica[0]==n and haslo==zgadywana:
                    return haslo, ilosc_ruchow, True
                else:
                    return haslo, ilosc_ruchow, False
       
        for liczba in mozliwe_liczby:
            if liczba == zapychacz1[0]:
                AktualnyZapychacz=zapychacz2
            else:
                AktualnyZapychacz=zapychacz1

            if liczba==mozliwe_liczby[-1]:
                for miejsce in miejsca:
                    haslo[miejsce]=liczba
                return funkcja_pomocnicza(haslo, zgadywana, n, ilosc_ruchow)

            for miejsce in miejsca:
                if len(miejsca)==1:
                    haslo[miejsce] = liczba
                    return funkcja_pomocnicza(haslo, zgadywana, n, ilosc_ruchow)
                proba = [AktualnyZapychacz[0]] * n
                proba[miejsce] = liczba
                print("Próba:", "".join(map(str, proba)))
                if Tryb_Gry==1:
                    tablica = InfoZwrotne(proba, zgadywana, n)
                else:
                    while(True):
                        tablica=[input("Podaj liczbę cyfr na właściwych miejscach: "), input("Podaj liczbę cyfr na niewłaściwych miejscach: ")]
                        if PoprawnoscInformacji(tablica[0], tablica[1], n):
                            tablica[0]=int(tablica[0])
                            tablica[1]=int(tablica[1])
                            break
                ilosc_ruchow += 1
                if tablica[0] == 1+AktualnyZapychacz[1]:
                    haslo[miejsce] = liczba
                    miejsca.remove(miejsce)  
                    break
                elif miejsce==miejsca[-2]:
                    haslo[miejsca[-1]]=liczba
                    miejsca.remove(miejsca[-1])
                    break
        return funkcja_pomocnicza(haslo, zgadywana, n, ilosc_ruchow)

    def zgadywanie(zgadywana: list, n: int):
    """
    Główna funkcja obsługująca proces zgadywania szyfru przez komputer.
    Funkcja łączy procesy szukania możliwych liczb i ustalania ich miejsc.
    Na podstawie otrzymanej informacji zwrotnej komputer próbuje odgadnąć szyfr.

    Argumenty:
        @ zgadywana: Lista zawierająca szyfr, który komputer ma odgadnąć.
        @ n: Długość szyfru.

    Zwraca:
         -Odgadnięty szyfr (lub przypuszczenie komputera).
         -Liczba prób potrzebnych do odgadnięcia.
         -True, jeśli szyfr został poprawnie odgadnięty, False w przeciwnym przypadku.

    Przykład:
        >>> zgadywanie([2, 0, 3, 1], 4)
        ([2, 0, 3, 1], 7, True)
    """
        IZ = szukanie_liczb(zgadywana) #IZ - Informacja zwrotna
        krok = IZ[1]
        if len(set(IZ[0]))==1:
            haslo = [IZ[0][0]] * n
            if haslo == zgadywana:
                return haslo, krok, True
            else:
                return haslo, krok, False
        else:
            haslo = [ int(IZ[2][0]) ] * n
            x = szukanie_miejsca(haslo, IZ[0], zgadywana, IZ[1], IZ[2], IZ[3])
            haslo = x[0]
            krok = x[1]
        return haslo, krok, x[2]
    
    while(True):
        zgadywana = input("Podaj szyfr: ")
        if not(PoprawnoscProby(zgadywana, n)):
            break
    zgadywana=(list[int](zgadywana))
    for i in range(n):
        zgadywana[i]=int(zgadywana[i])

    wynik = zgadywanie(zgadywana, n)
    if wynik[2]:
        print(f"Komputer odgadł szyfr: {"".join(map(str, wynik[0]))} w liczbie prób: {wynik[1]}")
    else:
        print(f"Komputer nie mógł odgadnąć szyfru, bo podano nieprawdziwą informację zwrotną")