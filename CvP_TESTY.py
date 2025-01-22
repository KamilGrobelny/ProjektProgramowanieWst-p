import FunkcjeZgadywanka as FZ
from random import randint
n = int(input("Podaj długość hasła (n): "))
#if n > 10 or n < 1:
#    raise ValueError("n musi być liczbą całkowitą z przedziału [1, 10]")

def szukanie_liczb(zgadywana: list[int]):
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
        #print("Próba:", "".join(map(str, proba))) #na czas testów pomijamy to, żeby nie zaśmiecało outputu
        tablica = FZ.InfoZwrotne(proba, zgadywana, n)
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
    """Funkcja ustala miejsca dla poprawnych liczb w hasle."""
    miejsca = list(range(n))

    def funkcja_pomocnicza(haslo, zgadywana, n, ilosc_ruchow):
        ilosc_ruchow+=1
        if FZ.InfoZwrotne(haslo, zgadywana, n)[0]==n:
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

            #print("Próba:", "".join(map(str, proba))) #to też pomijamy na czas testów

            tablica = FZ.InfoZwrotne(proba, zgadywana, n)
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
    """Główna funkcja obsługująca proces zgadywania.""" 
    IZ = szukanie_liczb(zgadywana) #IZ - Informacja zwrotna
    krok = IZ[1]
    if len(IZ[0])==1:
        haslo = [IZ[0]] * n
    else:
        haslo = [ int(IZ[2][0]) ] * n
        x = szukanie_miejsca(haslo, IZ[0], zgadywana, IZ[1], IZ[2], IZ[3])
        haslo = x[0]
        krok = x[1]
    return haslo, krok, x[2]

liczba=int(input("podaj liczbę prób: "))
for i in range(liczba):
    zgadywana = []
    #poniższą pętlę można wykasować i wprowadzać zgadywaną na sztywno, żeby sprawdzić konkretne przypadki i znaleźć słabość algorytmu
    for j in range (n):
        zgadywana.append(randint(0, 9))
    x = zgadywanie(zgadywana, n)
    if x[2]:
        print(f"SZYFR: {zgadywana} odgadnięcie: {x[0]} liczba prób: {x[1]}")
    else:
        print(f"Podano fałszywe informacje. SZYFR: {zgadywana}, NIEPRAWIDŁOWE ODGADNIĘCIE: {x[0]}, liczba prób: {x[1]}")