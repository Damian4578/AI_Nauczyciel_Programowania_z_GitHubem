```python
# Przykładowy kod systemu monitorowania temperatury
def monitoruj_temperature(temperatura):
    if temperatura > 30:
        print("Alarm: temperatura przekroczyła 30 stopni Celsjusza")
    else:
        print("Temperatura w normie")

# Przykładowy kod systemu podejmującego decyzję o korekcji trajektorii lotu
def korekcja_trajektorii(prędkość, wysokość, kierunek):
    if prędkość > 1000 and wysokość < 1000:
        print("Korekcja trajektorii lotu: zwiększ prędkość")
    elif prędkość < 500 and wysokość > 5000:
        print("Korekcja trajektorii lotu: zmniejsz prędkość")
    else:
        print("Trajektoria lotu w normie")

# Przykładowy kod systemu podejmującego decyzję o awaryjnym przerwaniu misji
def awaryjne_przerwanie_misji(prędkość, wysokość, kierunek):
    if prędkość > 2000 and wysokość < 500:
        print("Awaryjne przerwanie misji: raketa jest zbyt blisko Ziemi")
    elif prędkość < 100 and wysokość > 10000:
        print("Awaryjne przerwanie misji: raketa jest zbyt daleko od Ziemi")
    else:
        print("Misja w toku")
```