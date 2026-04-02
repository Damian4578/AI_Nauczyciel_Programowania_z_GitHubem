```python
def oblicz_prędkość_końcową(u, a, t):
    V = u + a * t
    return V

def oblicz_czas(u, V, a):
    t = (V - u) / a
    return t

# Misja 1
u = 200  # m/s
a = 10   # m/s^2
t = 5    # s
V = oblicz_prędkość_końcową(u, a, t)
print(f"Prędkość końcowa: {V} m/s")

# Misja 2
u = 100  # m/s
V = 500  # m/s
a = 20   # m/s^2
t = oblicz_czas(u, V, a)
print(f"Czas: {t} s")

# Misja 3
u = float(input("Podaj prędkość początkową (m/s): "))
a = float(input("Podaj przyspieszenie (m/s^2): "))
t = float(input("Podaj czas (s): "))
V = oblicz_prędkość_końcową(u, a, t)
print(f"Prędkość końcowa: {V} m/s")
```