# Computer vs Player dla 4 powinien zgadywać w 16 ruchach, trzeba printa dobrze zrobić"

haslo = ['x', 'x', 'x', 'x']
dobre_liczby = 0
liczby_na_swoim_miejscu = 0
ilosc_ruchow = 0
zapychacz = 0 #liczba, o której wiemy, że jej nie ma

n = int(input("podaj n: "))
if (n > 10) or (n < 1):
    raise ValueError("n musi być liczbą całowitą z przedziału [1, 10]")
zgadywana = []


def szukanie_liczb():
    global ilosc_ruchow, zapychacz
    mozliwe_liczby=[]
    dostepne_liczby=[0,1,2,3,4,5,6,7,8,9]
    for i in range(0, 9):
        if len(mozliwe_liczby)==4
            return mozliwe_liczby
        proba = int(str(i) * n)
        print(proba)
        dobre_liczby = int(input("Ile lczb jest poprawnych?"))
        liczby_na_swoim_miejscu = int(input("Ile liczb jest na swoime miejscu?"))
        ilosc_ruchow+=1
        if dobre_liczby !=0:
            for j in range(dobre_liczby):
                mozliwe_liczby.append(i)
        else:
            zapychacz = str(proba)[0]
            dostepne_liczby.remove(int(str(proba)[0]))
    return mozliwe_liczby

def szukanie_miejsca(liczby):
    global ilosc_ruchow
    miejsca =[i for i in range(0, n)]
    for liczba in liczby:
        for miejsce in miejsca:
            proba = int(miejsce*str(zapychacz) + str(liczba) + (n-1-miejsce)*str(zapychacz))
            print(proba)
            dobre_liczby = int(input("Ile lczb jest poprawnych?"))
            liczby_na_swoim_miejscu = int(input("Ile liczb jest na swoime miejscu?"))
            ilosc_ruchow += 1
            if liczby_na_swoim_miejscu == 1:
                miejsca.remove(miejsce)
                haslo[miejsce] = liczba
                break

def zgadywanie():
    liczby = szukanie_liczb()
    szukanie_miejsca(liczby)
    proba = int("".join(map(str, haslo)))
    print(proba)
    print(ilosc_ruchow)
zgadywanie()
