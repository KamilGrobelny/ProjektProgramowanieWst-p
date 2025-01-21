import FunkcjeZgadywanka as FZ
from random import randint
ilosc_ruchow = 0
n = int(input("Podaj długość hasła (n): "))
#if n > 10 or n < 1:
#    raise ValueError("n musi być liczbą całkowitą z przedziału [1, 10]")

def szukanie_liczb(zgadywana: list):
    global ilosc_ruchow, zapychacz1, zapychacz2
    zapychacz1 = [9, 0]
    zapychacz2 = [8, 0]
    mozliwe_liczby = []
    dostepne_liczby = list(range(10))  
    for i in dostepne_liczby:
        if len(mozliwe_liczby)==n:
            return mozliwe_liczby
        proba = [i] * n
        #print("Próba:", "".join(map(str, proba))) #na czas testów pomijamy to, żeby nie zaśmiecało outputu
        tablica = FZ.InfoZwrotne(proba, zgadywana, n)
        ilosc_ruchow += 1
        if i==zapychacz1[0]:
            JestZapychaczem1=True
            JestZapychaczem2=False
        elif i==zapychacz2[0]:
            JestZapychaczem2=True
            JestZapychaczem1=False
        else:
            JestZapychaczem1=False
            JestZapychaczem2=False
    
        if tablica[1] > 0:
            mozliwe_liczby.extend([i] * tablica[1])

        if tablica[0] > 0:
            mozliwe_liczby.extend([i] * tablica[0])
            if JestZapychaczem1:
                zapychacz1[1]+=tablica[0]
            elif JestZapychaczem2:
                zapychacz2[1]+=tablica[0]

    return mozliwe_liczby

def szukanie_miejsca(mozliwe_liczby, zgadywana: list):
    """Funkcja ustala miejsca dla poprawnych liczb w hasle."""
    global ilosc_ruchow, zapychacz1, zapychacz2
    miejsca = list(range(n)) 
    AktualnyZapychacz=zapychacz1
    for liczba in mozliwe_liczby:
        if liczba == zapychacz1[0]:
            AktualnyZapychacz=zapychacz2
        for miejsce in miejsca:
            proba = [AktualnyZapychacz[0]] * n
            proba[miejsce] = liczba
            #print("Próba:", "".join(map(str, proba))) #to też pomijamy na czas testów
            tablica = FZ.InfoZwrotne(proba, zgadywana, n)
            ilosc_ruchow += 1
            if tablica[0] == 1+AktualnyZapychacz[1]:
                haslo[miejsce] = liczba
                miejsca.remove(miejsce)  
                break

def zgadywanie(zgadywana: list):
    """Główna funkcja obsługująca proces zgadywania."""
    global haslo
    haslo = ['x'] * n 

    mozliwe_liczby = szukanie_liczb(zgadywana)

    szukanie_miejsca(mozliwe_liczby, zgadywana)

    finalna_proba = "".join(map(str, haslo))
    if zgadywana != haslo:
        print(f"!!!SOMETHING HAPPENS for {zgadywana}, returned {haslo} in {ilosc_ruchow} steps")
    else:
        print(f"Nothing happens for {zgadywana}, returned {haslo} in {ilosc_ruchow} steps")

ilosc_prob=int(input("podaj liczbę losowych przykładów, które chcesz sprawdzić: "))
for i in range(ilosc_prob):
    zgadywana = []
    #poniższą pętlę można wykasować i wprowadzać zgadywaną na sztywno, żeby sprawdzić konkretne przypadki i znaleźć słabość algorytmu
    for j in range (n):
        zgadywana.append(randint(0, 9))
    zgadywanie(zgadywana)
    ilosc_ruchow = 0
