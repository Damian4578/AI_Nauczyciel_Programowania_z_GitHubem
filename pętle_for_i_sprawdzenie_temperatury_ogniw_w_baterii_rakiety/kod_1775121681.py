```python
# Zadanie 1: Pętla for
def sprawdz_temperatura(temperatury):
    for temperatura in temperatury:
        if temperatura > 40:
            print(f"Temperatura {temperatura} jest za wysoka")
        else:
            print(f"Temperatura {temperatura} jest w normie")

# Zadanie 2: Sprawdzenie temperatury ogniw w baterii rakiety
def sprawdz_ogniwa(ogniwa):
    for i, temperatura in enumerate(ogniwa):
        if temperatura > 45:
            print(f"Ogniwo {i+1} ma temperaturę {temperatura}, która jest za wysoka")
        else:
            print(f"Ogniwo {i+1} ma temperaturę {temperatura}, która jest w normie")

# Zadanie 3: Wyświetlenie średniej temperatury ogniw
def srednia_temperatura(ogniwa):
    suma = sum(ogniwa)
    srednia = suma / len(ogniwa)
    print(f"Średnia temperatura ogniw wynosi {srednia}")

# Testowanie funkcji
temperatury = [30, 40, 50, 20, 35]
ogniwa = [42, 38, 48, 32, 40]
sprawdz_temperatura(temperatury)
sprawdz_ogniwa(ogniwa)
srednia_temperatura(ogniwa)
```