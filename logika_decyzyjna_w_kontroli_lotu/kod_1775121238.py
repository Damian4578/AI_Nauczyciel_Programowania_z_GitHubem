```python
# Zadanie 1: Symulacja systemu kontroli lotu
def kontrola_lotu(prędkość, wysokość):
    if prędkość > 500 and wysokość > 1000:
        return "Lot stabilny"
    elif prędkość < 200 and wysokość < 500:
        return "Lot niestabilny"
    else:
        return "Lot w trybie awaryjnym"

print(kontrola_lotu(600, 1200))  # Lot stabilny
print(kontrola_lotu(150, 300))   # Lot niestabilny
print(kontrola_lotu(400, 800))    # Lot w trybie awaryjnym

# Zadanie 2: Wybór trybu lotu
def wybór_trybu_lotu(prędkość, wysokość):
    if prędkość > 800 and wysokość > 2000:
        return "Tryb lotu: Auto-pilot"
    elif prędkość < 300 and wysokość < 800:
        return "Tryb lotu: Ręczny"
    else:
        return "Tryb lotu: Asystent"

print(wybór_trybu_lotu(900, 2500))  # Tryb lotu: Auto-pilot
print(wybór_trybu_lotu(200, 600))    # Tryb lotu: Ręczny
print(wybór_trybu_lotu(500, 1200))    # Tryb lotu: Asystent

# Zadanie 3: Symulacja systemu ostrzegania
def system_ostrzegania(prędkość, wysokość):
    if prędkość > 1000 and wysokość > 3000:
        return "Ostrzeżenie: Przekroczenie prędkości i wysokości"
    elif prędkość < 100 and wysokość < 300:
        return "Ostrzeżenie: Niski poziom prędkości i wysokości"
    else:
        return "Brak ostrzeżeń"

print(system_ostrzegania(1100, 3500))  # Ostrzeżenie: Przekroczenie prędkości i wysokości
print(system_ostrzegania(50, 200))      # Ostrzeżenie: Niski poziom prędkości i wysokości
print(system_ostrzegania(500, 1200))    # Brak ostrzeżeń
```