## Ćwiczenia do Wykonania

1. Napisz program, który przyjmie liczbę od użytkownika i wypisze, czy liczba ta jest parzysta czy nieparzysta, czy jest dodatnia, ujemna, czy równa zero. Użyj operatorów logicznych do sprawdzenia warunków oraz pętli do weryfikacji czynników liczby pierwszej. W celu przyjęcia danych od użytkiownika należy wykorszystać wbdowaną funkcję `input()`. Przykład wykorzystania funkcji `input()`:
    ```python
    # Prośba o wpisanie imienia użytkownika
    imie = input("Jak masz na imię? ")

    # Wypisanie powitania z imieniem podanym przez użytkownika
    print(f"Cześć, {imie}! Miło Cię poznać.")

    # Prośba o wpisanie wieku użytkownika
    wiek = input("Ile masz lat? ")

    # Konwersja wieku z tekstu na liczbę całkowitą
    wiek = int(wiek)

    # Wypisanie informacji zwrotnej z wiekiem użytkownika
    print(f"Okej, masz {wiek} lat. To znaczy, że urodziłeś się w roku {2023 - wiek}.")
    ```

2. Napisz program w języku Python, który symuluje proces sprawdzania stanu portów na serwerze. Program powinien przejrzeć porty od 1 do 50 i dla każdego z nich wykonać następujące czynności:
    - Jeżeli numer portu jest **parzysty**, uznaj port za "zamknięty" i wydrukuj informację o tym.
    - Jeżeli numer portu jest **nieparzysty**, uznaj port za "otwarty" i wydrukuj informację.
    - Gdy program natrafi na port o numerze **22** (SSH), powinien wydrukować komunikat "Bezpieczny port SSH znaleziony, kontynuuję skanowanie..." i kontynuować działanie bez przerywania pętli.
    - Jeśli program dojdzie do portu o numerze **50**, powinien wydrukować "Zakończono skanowanie portów" i zakończyć działanie programu.

    Wykorzystaj pętlę `for` i funkcję `range()`.

### Przykładowe Rozwiązania

#### Zadanie 1.

```python
# Prośba o wpisanie liczby przez użytkownika
tekst_wejsciowy = input("Podaj liczbę: ")

# Konwersja wprowadzonego tekstu na liczbę całkowitą
liczba = int(tekst_wejsciowy)

# Sprawdzanie, czy liczba jest równa zero
if liczba == 0:
    print("Liczba jest równa zero")
else:
    # Liczba jest różna od zera, sprawdzamy czy jest dodatnia czy ujemna
    if liczba > 0:
        print("Liczba jest dodatnia")
    else:
        print("Liczba jest ujemna")
    
    # Sprawdzanie parzystości liczby
    if liczba % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")

```

```
Podaj liczbę: 7    <-- przykład
Liczba jest dodatnia
Liczba jest nieparzysta
```

#### Zadanie 2.

```python
for port in range(1, 51):  # Przechodzenie przez listę portów od 1 do 50
    if port == 22:  # Jeśli port to 22
        print("Bezpieczny port SSH znaleziony, kontynuuję skanowanie...")
        continue
    elif port % 2 == 0:  # Jeśli numer portu jest parzysty
        print(f"Port {port} jest zamknięty.")
    else:  # Jeśli numer portu jest nieparzysty
        print(f"Port {port} jest otwarty.")
    
    if port == 50:  # Jeśli port to 50
        print("Zakończono skanowanie portów")
        break

```

```
Port 1 jest otwarty.
Port 2 jest zamknięty.
Port 3 jest otwarty.
Port 4 jest zamknięty.
...
Bezpieczny port SSH znaleziony, kontynuuję skanowanie...
...
Port 48 jest zamknięty.
Port 49 jest otwarty.
Port 50 jest zamknięty.
Zakończono skanowanie portów
```

