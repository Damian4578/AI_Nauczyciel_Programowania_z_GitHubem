```python
# Zadanie 1: Pętla for
def sprawdz_temperature(temperatury):
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

# Zadanie 3: Symulacja sprawdzenia temperatury ogniw w baterii rakiety
def symulacja_sprawdzenia():
    temperatury = [30, 40, 50, 20, 35]
    ogniw = [42, 38, 48, 32, 40]
    sprawdz_temperature(temperatury)
    sprawdz_ogniwa(ogniwa)

symulacja_sprawdzenia()
```