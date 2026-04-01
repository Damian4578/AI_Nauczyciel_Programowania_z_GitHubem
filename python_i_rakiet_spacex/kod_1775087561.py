import random

def suma_listy(lista):
    return sum(lista)

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

def losowa_liczba():
    return random.randint(1, 100)

print(suma_listy([1, 2, 3, 4, 5]))  # 15
print(czy_pierwsza(11))  # True
print(losowa_liczba())  # losowa liczba między 1 a 100