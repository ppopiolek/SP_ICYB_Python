## Ćwiczenia do wykonania

1. W dziedzinie cyberbezpieczeństwa, Systemy zarządzania informacjami i zdarzeniami z zakresu bezpieczeństwa (SIEM) są kluczowym elementem infrastruktury bezpieczeństwa. Dla zespołu odpowiedzialnego za bezpieczeństwo, ważne jest zrozumienie, jak koszty zakupu takich systemów wpływają na miesięczny budżet. 
   
   Przyjmijmy, że nasz zespół rozważa zakup subskrypcji na system SIEM, który kosztuje 90 tys. dolarów amerykańskich rocznie. Twoim zadaniem jest obliczenie, ile realnie kwoty ubędzie z miesięcznego budżetu zespołu (w złotówkach), biorąc pod uwagę ten zakup.
   
   Przyjmujemy uproszczony kurs wymiany USD/PLN na poziomie 4.20. 

2. Pracując w dziale cyberbezpieczeństwa, często spotkasz się z sytuacjami, gdzie musisz analizować różne zagrożenia i podejmować decyzje na podstawie dostępnych danych. W tym zadaniu wykorzystamy operatory logiczne `and`, `or` oraz `not`, aby przeanalizować różne scenariusze zagrożeń.

   Przykładowe scenariusze:
   - `zagrozenie_1` oznacza, że system wykrył podejrzane połączenie sieciowe.
   - `zagrozenie_2` oznacza, że system wykrył podejrzane pliki na serwerze.
   - `zagrozenie_3` oznacza, że system wykrył nieautoryzowany dostęp do bazy danych.
    
   Przyjmij, że wykryto następujące wartości dla badanych zagrożeń:
   
    ```python
    zagrozenie_1 = True
    zagrozenie_2 = False
    zagrozenie_3 = True
    ```

   Twoim zadaniem jest sprawdzenie:
   - Czy istnieje jednocześnie podejrzane połączenie sieciowe i podejrzane pliki na serwerze?
   - Czy istnieje podejrzane połączenie sieciowe lub nieautoryzowany dostęp do bazy danych?
   - Czy nie ma żadnego zagrożenia związanego z podejrzanymi plikami na serwerze?

3. Porównywanie stringów:
    - Przypisz wartość "Python" do zmiennej `str1` i wartość "python" do zmiennej `str2`. Sprawdź i wypisz wyniki porównania tych dwóch stringów pod kątem równości, nierówności, a także sprawdź porządek leksykograficzny. Sprawdź również, jak zachowają się te porównania po użyciu funkcji `lower()` na obu stringach.

    - Nastepnie przypisz wartość "apple" do zmiennej `str3` i wartość "banana" do zmiennej `str4`. Sprawdź i wypisz wyniki porównania tych dwóch stringów pod kątem równości, nierówności, a także sprawdź porządek leksykograficzny.

    - Sprawdź teraz, czy `str3` jest prefiksem dla `str4`. W tym celu skorzystaj z funkcji `startswith()`.

    

### Przykładowe rozwiązania

#### Zadanie 1.
```python
roczny_koszt_siema_usd = 90000
kurs_wymiany_usd_pln = 4.20
miesieczny_koszt_siema_pln = (roczny_koszt_siema_usd * kurs_wymiany_usd_pln) / 12
print(f"Miesięczny koszt SIEM w PLN: {miesieczny_koszt_siema_pln:.2f} zł")
```

```
Miesięczny koszt SIEM w PLN: 31500.00 zł
 ```

#### Zadanie 2.

```python
zagrozenie_1 = True
zagrozenie_2 = False
zagrozenie_3 = True
print("Czy istnieje jednocześnie podejrzane połączenie sieciowe i podejrzane pliki na serwerze?", zagrozenie_1 and zagrozenie_2)
print("Czy istnieje podejrzane połączenie sieciowe lub nieautoryzowany dostęp do bazy danych?", zagrozenie_1 or zagrozenie_3)
print("Czy nie ma żadnego zagrożenia związanego z podejrzanymi plikami na serwerze?", not zagrozenie_2)
```
```python
zagrozenie_1 = True
zagrozenie_2 = False
zagrozenie_3 = True
print("Czy zagrożenie 1 i 2 występują razem?", zagrozenie_1 and zagrozenie_2)
print("Czy występuje zagrożenie 1 lub 3?", zagrozenie_1 or zagrozenie_3)
print("Czy brak zagrożenia 2?", not zagrozenie_2)
```

```
Czy zagrożenie 1 i 2 występują razem? False
Czy występuje zagrożenie 1 lub 3? True
Czy brak zagrożenia 2? True
```
#### Zadanie 3.

- część 1.
    
    ```python
    str1 = "Python"
    str2 = "python"
    print("Równość:", str1 == str2)
    print("Nierówność:", str1 != str2)
    print("Porządek leksykograficzny (str1 < str2):", str1 < str2)
    print("Porządek leksykograficzny po lower() (str1 < str2):", str1.lower() < str2.lower())
    ```

    ```
    Równość: False
    Nierówność: True
    Porządek leksykograficzny (str1 < str2): False
    Porządek leksykograficzny po lower() (str1 < str2): False
    ```
- część 2.

    ```python
    str3 = "apple"
    str4 = "banana"
    print("Równość:", str3 == str4)
    print("Nierówność:", str3 != str4)
    print("Porządek leksykograficzny (str3 < str4):", str3 < str4)
    ```

    ```
    Równość: False
    Nierówność: True
    Porządek leksykograficzny (str3 < str4): True
    ```
- część 3.

    ```python
    print("Czy str3 jest prefiksem str4:", str4.startswith(str3))
    ```

    ```
    Czy str3 jest prefiksem str4: False
    ```
