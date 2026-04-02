```python
# Zadanie 1: Obliczanie prędkości rakietowej
def oblicz_prędkość_rakietową(masa_paliwa, masa_rakiety, czas_spalania):
    """
    Oblicza prędkość rakietową na podstawie masy paliwa, masy rakiety i czasu spalania.
    """
    g = 9.81  # przyspieszenie ziemskie
    prędkość_rakietowa = (masa_paliwa / masa_rakiety) * g * czas_spalania
    return prędkość_rakietowa

# Zadanie 2: Symulacja lotu rakiety
def symulacja_lotu_rakiety(prędkość_rakietowa, wysokość_startowa, czas_lotu):
    """
    Symuluje lot rakiety na podstawie prędkości rakietowej, wysokości startowej i czasu lotu.
    """
    wysokość_bieżąca = wysokość_startowa
    for i in range(czas_lotu):
        wysokość_bieżąca += prędkość_rakietowa
        print(f"Czas: {i+1} s, Wysokość: {wysokość_bieżąca} m")

# Zadanie 3: Obliczanie kąta nachylenia rakiety
def oblicz_kąt_nachylenia_rakiety(prędkość_rakietowa, wysokość_bieżąca, odległość_do_celu):
    """
    Oblicza kąt nachylenia rakiety na podstawie prędkości rakietowej, wysokości bieżącej i odległości do celu.
    """
    kąt_nachylenia = (prędkość_rakietowa / (wysokość_bieżąca + odległość_do_celu)) * 180 / 3.14159
    return kąt_nachylenia

# Testowanie funkcji
masa_paliwa = 1000  # kg
masa_rakiety = 5000  # kg
czas_spalania = 10  # s
prędkość_rakietowa = oblicz_prędkość_rakietową(masa_paliwa, masa_rakiety, czas_spalania)
print(f"Prędkość rakietowa: {prędkość_rakietowa} m/s")

wysokość_startowa = 1000  # m
czas_lotu = 10  # s
symulacja_lotu_rakiety(prędkość_rakietowa, wysokość_startowa, czas_lotu)

odległość_do_celu = 5000  # m
kąt_nachylenia = oblicz_kąt_nachylenia_rakiety(prędkość_rakietowa, wysokość_startowa, odległość_do_celu)
print(f"Kąt nachylenia rakiety: {kąt_nachylenia} stopni")
```