```python
import random

def suma_liczb(liczby):
    return sum(liczby)

def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

def losowa_liczba():
    return random.randint(1, 100)

print(suma_liczb([1, 2, 3, 4, 5]))
print(czy_pierwsza(25))
print(losowa_liczba())
```