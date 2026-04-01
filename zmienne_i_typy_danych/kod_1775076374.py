```python
# deklaracja zmiennej typu string
imie = "Jan"

# deklaracja zmiennej typu integer
edad = 25

# deklaracja zmiennej typu float
zolw = 3.7

# deklaracja zmiennej typu boolean
woda = True

# wypisanie zmiennej na ekran
print("Cześć, na imię mnie zwać: ", imie)
print("I mam", edad, "lat")
print("Mam 3.7 litrów wody", end=' ')
print("i jestem zdrowy:", woda)

# deklaracja zmiennej typu list
kolory = ["niebieski","czerwony","zielony"]

# wypisanie elementów z listy
print("Przykładowe elementy listy to:\n", end='')
for kolor in kolory:
    print(kolor, end=', ')

# deklaracja zmiennej typu dictionary
osoby = {"Jan": 21,"Anna": 30,"Ola": 45}

# wypisanie elementów z słownika
print("\nPrzykładowe elementy słownika:\n")
for Imie, Wiek in osoby.items():
    print(Imie + " jest", Wiek, "lat.")
```