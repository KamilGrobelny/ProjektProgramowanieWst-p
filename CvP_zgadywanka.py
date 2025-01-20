import FunkcjeZgadywanka as FZ
from random import randint
ilosc_ruchow = 0
zapychacz = 0 #Liczba, o której wiemy, że jej nie ma 
n = int(input("Podaj długość hasła (n): "))
if n > 10 or n < 1:
    raise ValueError("n musi być liczbą całkowitą z przedziału [1, 10]")

def szukanie_liczb(zgadywana: list):
    global ilosc_ruchow, zapychacz
    mozliwe_liczby = []
    dostepne_liczby = list(range(10))  

    for i in dostepne_liczby:
        if len(mozliwe_liczby)==n:
            return mozliwe_liczby
        proba = [i] * n
        #print("Próba:", "".join(map(str, proba))) #na czas testów pomijamy to, żeby nie zaśmiecało outputu
        tablica = FZ.InfoZwrotne(proba, zgadywana, n)
        ilosc_ruchow += 1

        if tablica[1] > 0:
            mozliwe_liczby.extend([i] * tablica[1])
        if tablica[0] > 0:
            mozliwe_liczby.extend([i] * tablica[0])
        else:
            zapychacz = i
    return mozliwe_liczby

def szukanie_miejsca(mozliwe_liczby, zgadywana: list):
    """Funkcja ustala miejsca dla poprawnych liczb w hasle."""
    global ilosc_ruchow
    miejsca = list(range(n)) 

    for liczba in mozliwe_liczby:
        for miejsce in miejsca:
            proba = [zapychacz] * n
            proba[miejsce] = liczba
            #print("Próba:", "".join(map(str, proba))) #to też pomijamy na czas testów
            tablica = FZ.InfoZwrotne(proba, zgadywana, n)
            ilosc_ruchow += 1

            if tablica[0] == 1:
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
    print(f"SZYFR: {zgadywana}, Odgadnięte: {haslo}, ruchy {ilosc_ruchow}")
for i in range(100):
    zgadywana = []
    #poniższą pętlę można wykasować i wprowadzać zgadywaną na sztywno, żeby sprawdzić konkretne przypadki i znaleźć słabość algorytmu
    for j in range (n):
        zgadywana.append(randint(0, 9))
    zgadywanie(zgadywana)
    ilosc_ruchow = 0
