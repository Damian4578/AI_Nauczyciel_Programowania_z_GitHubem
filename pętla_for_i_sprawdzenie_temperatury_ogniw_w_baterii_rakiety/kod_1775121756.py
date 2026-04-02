```python
# Zadanie 1: Pętla For
def petla_for():
    # Wyświetl liczby od 1 do 10
    for i in range(1, 11):
        print(i)

# Zadanie 2: Sprawdzenie Temperatury Ogniw w Baterii Rakiety
def sprawdz_temperature(temperatury):
    # Ustaw maksymalną temperaturę
    max_temp = 40
    # Sprawdź temperatury ogniw
    for temperatura in temperatury:
        if temperatura > max_temp:
            print(f"Ostrzeżenie: temperatura {temperatura} przekracza maksymalną temperaturę {max_temp}")
        else:
            print(f"Temperatura {temperatura} jest w normie")

# Zadanie 3: Wyszukiwanie Maksymalnej Temperatury
def wyszukaj_max_temperature(temperatury):
    # Ustaw maksymalną temperaturę
    max_temp = max(temperatury)
    # Wyszukaj indeks maksymalnej temperatury
    index = temperatury.index(max_temp)
    print(f"Maksymalna temperatura {max_temp} występuje w ogniwie {index+1}")

# Uruchom zadania
petla_for()
temperatury = [30, 35, 40, 45, 50]
sprawdz_temperature(temperatury)
wyszukaj_max_temperature(temperatury)
```