from random import randint
import FunkcjeZgadywanka as FZ

# Player vs Player - zmieniłem funkcje Odgadywanie -ilosckrokow(a), if Wartosci[0] == n: ...
n = int(input("podaj n: "))
a=0
if (n > 10) or (n < 1):
    raise ValueError("n musi być liczbą całowitą z przedziału [1, 10]")
zgadywana = []
zgadywana1 = []
for i in range(n):
    zgadywana.append(randint(0, 9))
b=FZ.Odgadywanie(zgadywana, n, a)[0]
print("ZMIANA ZAWODNIKA.")
for i in range(n):
    zgadywana1.append(randint(0, 9))
c=FZ.Odgadywanie(zgadywana1, n, a)[0]
if (b<c):
    print("Wygrał 1 zawodnik.")
elif (b==c):
    print("Remis")
else:
    print("Wygrał 2 zawodnik.")