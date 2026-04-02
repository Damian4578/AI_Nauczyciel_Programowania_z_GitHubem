```python
def monitoruj_temperature(temperatura, próg):
    if temperatura > próg:
        return True
    else:
        return False

def oblicz_średnią_temperaturę(temperatury):
    return sum(temperatury) / len(temperatury)

def uruchom_system_chłodzenia(temperatura, próg):
    if temperatura > próg:
        return True
    else:
        return False
```