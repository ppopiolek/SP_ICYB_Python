## Ćwiczenia do wykonania

1. Zdefiniuj trzy zmienne: jedną typu string, jedną typu int i jedną typu float. Następnie wypisz ich typy przy pomocy funkcji `type()`.

2. Stwórz dwa stringi, a następnie połącz je ze sobą w jeden string. Wypisz wynik.


3. Mając dwie zmienne, `imie` i `wiek`, wypisz zdanie wykorzystując formatowanie stringów, które przy założeniu, że `imie` to "Jan" a `wiek` to 30, będzie wyglądało tak:
    ```
    Podane dane:

    Imię:    "Jan"
    Wiek:    30 lat
    ```

4. Zdefiniuj zmienne typu float, które są blisko tej samej wartości całkowitej, ale z różnymi częściami dziesiętnymi (np. `9.4`, `9.5`, `9.6`). Następnie dokonaj ich konwersji na typ int i obserwuj, jak zachowuje się zaokrąglenie. Dodatkowo dla tych samych liczb sprawdź, jak działa funkcja zaokraglenia `round()`.

### Przykładowe rozwiązania

#### Zadanie 1.

```python
# Zdefiniowanie zmiennych
napis = "Hello world!"
liczba_calkowita = 42
liczba_zmiennoprzecinkowa = 3.14

# Wypisanie typów zmiennych
print(type(napis))
print(type(liczba_calkowita))
print(type(liczba_zmiennoprzecinkowa))
```

```plaintext
<class 'str'>
<class 'int'>
<class 'float'>
```

#### Zadanie 2.

```python
# Definicja stringów
napis1 = "Python "
napis2 = "rządzi!"

# Połączenie stringów
wynik = napis1 + napis2

# Wypisanie wyniku
print(wynik)
```

```plaintext
Python rządzi!
```

#### Zadanie 3.

```python
# Definicja zmiennych
imie = "Jan"
wiek = 30

# Wypisanie zdania z formatowaniem
print(f"Podane dane:\n\nImię:\t\"{imie}\"\nWiek:\t{wiek} lat")
```

```plaintext
Podane dane:

Imię:    "Jan"
Wiek:    30 lat
```

#### Zadanie 4.

```python
# Definicja zmiennych
liczba1 = 9.4
liczba2 = 9.5
liczba3 = 9.6

# Konwersja do int
liczba_calkowita1 = int(liczba1)
liczba_calkowita2 = int(liczba2)
liczba_calkowita3 = int(liczba3)

print(f'Konwersja liczby {liczba1} na int: {liczba_calkowita1}')
print(f'Konwersja liczby {liczba2} na int: {liczba_calkowita2}')
print(f'Konwersja liczby {liczba3} na int: {liczba_calkowita3}')

# Zaokrąglenie
zaokraglona_liczba1 = round(liczba1)
zaokraglona_liczba2 = round(liczba2)
zaokraglona_liczba3 = round(liczba3)

print(f'Zaokrąglenie liczby {liczba1}: {zaokraglona_liczba1}')
print(f'Zaokrąglenie liczby {liczba2}: {zaokraglona_liczba2}')
print(f'Zaokrąglenie liczby {liczba3}: {zaokraglona_liczba3}')
```

```plaintext
Konwersja liczby 9.4 na int: 9
Konwersja liczby 9.5 na int: 9
Konwersja liczby 9.6 na int: 9
Zaokrąglenie liczby 9.4: 9
Zaokrąglenie liczby 9.5: 10
Zaokrąglenie liczby 9.6: 10
```
