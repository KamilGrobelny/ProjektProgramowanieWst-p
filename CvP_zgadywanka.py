haslo = ['x'] * 4  
ilosc_ruchow = 0
zapychacz = 0 #Liczba, o której wiemy, że jej nie ma

n = int(input("Podaj długość hasła (n): "))
if n > 10 or n < 1:
    raise ValueError("n musi być liczbą całkowitą z przedziału [1, 10]")

def szukanie_liczb():
    global ilosc_ruchow, zapychacz
    mozliwe_liczby = []
    dostepne_liczby = list(range(10))  

    for i in dostepne_liczby:
        if len(mozliwe_liczby)==n:
            return mozliwe_liczby
        proba = [i] * n
        print("Próba:", "".join(map(str, proba)))
        dobre_liczby = int(input("Ile liczb jest poprawnych? "))
        liczby_na_swoim_miejscu = int(input("Ile liczb jest na swoich miejscach? "))
        ilosc_ruchow += 1

        if dobre_liczby > 0:
            mozliwe_liczby.extend([i] * dobre_liczby)
        else:
            zapychacz = i
    return mozliwe_liczby

def szukanie_miejsca(mozliwe_liczby):
    """Funkcja ustala miejsca dla poprawnych liczb w hasle."""
    global ilosc_ruchow
    miejsca = list(range(n)) 

    for liczba in mozliwe_liczby:
        for miejsce in miejsca:
            proba = [zapychacz] * n
            proba[miejsce] = liczba
            print("Próba:", "".join(map(str, proba)))
            dobre_liczby = int(input("Ile liczb jest poprawnych? "))
            liczby_na_swoim_miejscu = int(input("Ile liczb jest na swoich miejscach? "))
            ilosc_ruchow += 1

            if liczby_na_swoim_miejscu == 1:
                haslo[miejsce] = liczba
                miejsca.remove(miejsce)  
                break

def zgadywanie():
    """Główna funkcja obsługująca proces zgadywania."""
    global haslo
    haslo = ['x'] * n 

    mozliwe_liczby = szukanie_liczb()

    szukanie_miejsca(mozliwe_liczby)

    finalna_proba = "".join(map(str, haslo))
    print(f"Odgadnięte hasło: {finalna_proba}")
    print(f"Liczba ruchów: {ilosc_ruchow}")

zgadywanie()