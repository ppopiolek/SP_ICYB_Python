## Ćwiczenia do Wykonania

1. Napisz funkcję `sprawdz_silne_haslo`, która przyjmuje hasło jako argument i zwraca `True`, jeśli hasło spełnia następujące kryteria dla silnego hasła:
    - ma co najmniej 8 znaków długości,
    - zawiera co najmniej jedną cyfrę,
    - zawiera co najmniej jedną wielką literę.

    Wykorzystaj funkcje `len()`, `any()` oraz metody `isdigit()` i `isupper()` do sprawdzenia tych warunków w hasle.

2. Napisz funkcję `rejestruj_aktywnosc`, która przyjmuje nazwę użytkownika oraz dowolną liczbę czasów logowania (reprezentowanych jako stringi z czasem) i drukuje komunikat z najwcześniejszym i najpóźniejszym czasem logowania dla danego użytkownika. Wykorzystaj funkcje `min()` i `max()` do znalezienia odpowiednich czasów.

    Użyj formatowania stringów, aby wygenerować czytelny komunikat, na przykład:
`"Użytkownik: [nazwa], Pierwsze logowanie: [czas], Ostatnie logowanie: [czas]".`

    **Uwaga**: Godziny w formie stringa, takie jak "08:00" czy "12:00", są porównywalne w Pythonie, ponieważ porównanie stringów odbywa się alfabetycznie, znak po znaku od lewej do prawej. W kontekście godzin w formacie HH:MM, jeśli stringi są w tym samym formacie, ich porównanie alfabetyczne (leksykograficzne) jest równoważne porównaniu czasowemu pod warunkiem, że oba stringi mają tę samą długość i są poprawnie sformatowane.
    
### Przykładowe rozwiązania

#### Zadaine 1.

```python
def sprawdz_silne_haslo(haslo):
    return (len(haslo) >= 8 and
            any(znak.isdigit() for znak in haslo) and
            any(znak.isupper() for znak in haslo))

# Testowanie funkcji
print(sprawdz_silne_haslo("SilneHaslo1")) 
print(sprawdz_silne_haslo("haslo"))       
```

```
True
False
```

#### Zadanie 2.

```python
def rejestruj_aktywnosc(nazwa_uzytkownika, czasy_logowania):
    najwczesniejsze_logowanie = min(czasy_logowania)
    najpozniejsze_logowanie = max(czasy_logowania)
    print(f"Użytkownik: {nazwa_uzytkownika}, Pierwsze logowanie: {najwczesniejsze_logowanie}, Ostatnie logowanie: {najpozniejsze_logowanie}")

# Testowanie funkcji
rejestruj_aktywnosc("jankowalski", ["08:00", "12:00", "18:00"])

```

```
Użytkownik: jankowalski, Pierwsze logowanie: 08:00, Ostatnie logowanie: 18:00
```
