# Zadanie Laboratoryjne: Łamanie haseł za pomocą skryptu w Pythonie

## Kontekst zadania

Grupa została zatrudniona do przeprowadzenia testów penetracyjnych zabezpieczeń pewnej organizacji. Po szczegółowej analizie i wstępnym rozpoznaniu, udało się zlokalizować formularz logowania na stronie, który może stanowić słaby punkt systemu bezpieczeństwa. Aby kontynuować testy, należy stworzyć listę słów (wordlistę) i użyć jej do próby złamania zabezpieczeń dostępowych do konta na tej stronie.

Formularz logowania znajduje się pod adresem: [https://ppopiolek.github.io/brute-force-app](https://ppopiolek.github.io/brute-force-app). Strona została zabezpieczona, a wszystkie hasła są przechowywane w formie hashowanej. **Jednak ktoś z administracji popełnił błąd** i hasła są publicznie dostępne pod adresem:  
[https://ppopiolek.github.io/brute-force-app/passwords.json](https://ppopiolek.github.io/brute-force-app/passwords.json). 
To oznacza, że można pobrać ten plik i łamać hashe lokalnie. Dzięki temu, zamiast próbować złamać zabezpieczenia bezpośrednio przez stronę, możliwe jest porównywanie wygenerowanych hashy z hashami znajdującymi się w tym pliku.

### Na czym polega atak słownikowy?

**Atak słownikowy** to metoda łamania haseł, która polega na próbie dopasowania hasła do jego skrótu (hashu) poprzez generowanie i sprawdzanie całej listy potencjalnych haseł (tzw. wordlisty). Lista ta zazwyczaj zawiera słowa lub ich warianty, które ludzie często stosują jako hasła, np. "password123", "admin!", "qwerty2023". Atak słownikowy jest skuteczny, gdy hasło jest popularne lub łatwe do przewidzenia.

### Zadanie dla grup

W zadaniu kaźdy będzie miał dostęp do listy hashy użytkowników w pliku `passwords.json`. **Każdemu zostanie przypisane jedno hasło (jeden hash) do złamania**. Celem jest wygenerowanie wordlisty i takiego wariantu haseł, aby hash wybranego użytkownika znalazł swoje dopasowanie. Innymi słowy, należy "zgadnąć" hasło, aż nie zostanie znalezione dopasowanie. Głównym celem jest wykorzystanie różnych konstrukcji Pythona i iteracyjne budowanie coraz bardziej złożonego skryptu.  

---

## Cele zadania

Wynikiem zadania będzie:
1. **Działający skrypt w Pythonie**, który generuje wordlistę opartą na treści strony internetowej oraz odpowiednich permutacjach.
2. **Wordlista** wygenerowana przez skrypt, gotowa do użycia w ataku słownikowym.
3. Logowanie na stronę [https://ppopiolek.github.io/brute-force-app](https://ppopiolek.github.io/brute-force-app) uzyskanym hasłem.

---

## Iteracyjne rozwijanie skryptu

Poniżej znajdują się kolejne etapy budowania skryptu. Każda sekcja zawiera wskazówki i częściowy kod, który należy uzupełnić. Cały szkielet jest dostępny na końcu instrukcji jako baza do pracy.

### Iteracja 1: Pobranie HTML strony

**Cel**: Utworzenie funkcji `get_html_of`, która pobierze kod HTML z podanego adresu URL i wyświetli go.

**Wskazówka**: Użyj biblioteki `requests`, aby pobrać stronę. Sprawdź kod statusu odpowiedzi (status code 200 oznacza powodzenie).

```python
import requests

def get_html_of(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'Błąd pobierania strony: kod {resp.status_code}')
        exit(1)
    return resp.content.decode()

# Test
print(get_html_of('https://en.wikipedia.org/wiki/Warsaw_University_of_Technology'))
```

---

### Iteracja 2: Wyodrębnienie czystego tekstu ze strony

**Cel**: Dodanie funkcji `get_all_words_from`, która pobierze tekst strony, usunie tagi HTML i wyodrębni same słowa.

**Wskazówka**: Użyj `BeautifulSoup` do usunięcia HTML, a `re.findall()` do wyciągnięcia słów.

```python
from bs4 import BeautifulSoup
import re

def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    # Zwracamy tylko słowa o długości co najmniej 5 znaków
    return [word for word in re.findall(r'\w+', raw_text) if len(word) >= 5]


# Test
all_words = get_all_words_from('https://en.wikipedia.org/wiki/Warsaw_University_of_Technology')
print(all_words[:10])  # wyświetl pierwsze 10 słów
```

---

### Iteracja 3: Zliczanie i sortowanie słów

**Cel**: Stworzenie funkcji `count_occurrences_in`, która policzy wystąpienia każdego słowa w liście słów i zwróci listę posortowaną od najczęściej do najrzadziej występujących.

**Wskazówka**: Użyj słownika do zliczania wystąpień słów.

```python
def count_occurrences_in(word_list):
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Test
occurrences = count_occurrences_in(all_words)
print(occurrences[:10])  # wyświetla 10 najczęstszych słów
```

---

### Iteracja 4: Dodawanie podstawowych mutacji słów

**Cel**: Dodanie funkcji `generate_password_mutations`, która wygeneruje podstawowe warianty słowa.

**Mutacje do zaimplementowania**:
1. Wersja oryginalna, słowo zaczynające się wielką literą, słowo pisane wielkimi literami.
2. Dodanie popularnych zakończeń, takich jak `123`, `!`, `@2023`.

```python
def generate_password_mutations(word):
    mutations = [word, word.capitalize(), word.upper()]
    # Dodanie popularnych zakończeń
    for suffix in ["123", "!", "@2023"]:
        mutations.append(word + suffix)
    return mutations

# Test
print(generate_password_mutations("example"))
```

---

### Iteracja 5: Rozbudowa mutacji

**Cel**: Dodanie bardziej zaawansowanych wariantów do funkcji `generate_password_mutations`.

**Mutacje do zaimplementowania**:
1. Powtórzenie słowa, np. `wordword` i `WordWORD`.
2. Losowe mieszanie wielkości liter w słowie, np. `eXaMpLe`.
3. Dodanie dodatkowych znaków na końcu.

```python
import random

def generate_password_mutations(word):
    mutations = [word, word.capitalize(), word.upper(), word + "123", word + "!", word + "@2023"]
    # Powtórzenie słowa
    mutations.append(word * 2)
    mutations.append(word.capitalize() + word.upper())
    # Losowe mieszanie wielkości liter
    mutations.append(''.join(random.choice((str.upper, str.lower))(c) for c in word))
    return mutations

# Test
print(generate_password_mutations("example"))
```

---

### Iteracja 6: Tworzenie i zapisywanie wordlisty

**Cel**: Połączenie wszystkich powyższych funkcji i zapisanie wygenerowanej wordlisty do pliku `.txt`.

```python
def save_to_file(word_list, filename):
    with open(filename, 'w') as file:
        for word in word_list:
            file.write(word + '\n')
    print(f"Wyniki zapisane do {filename}")

# Przykład zapisu do pliku
words_with_mutations = generate_password_mutations("example")
save_to_file(words_with_mutations, "wordlist.txt")
```

---

## Kompletny kod szkieletu do skopiowania

```python
import requests
from bs4 import BeautifulSoup
import re
import random

# Pobiera HTML strony
def get_html_of(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f'Błąd pobierania strony: kod {resp.status_code}')
        exit(1)
    return resp.content.decode()

# Wyodrębnia słowa ze strony
def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    return [word for word in re.findall(r'\w+', raw_text) if len(word) >= 5]

# Zlicza wystąpienia słów
def count_occurrences_in(word_list):
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

# Generuje mutacje dla słowa
def generate_password_mutations(word):
    mutations = [word, word.capitalize(), word.upper(), word + "123", word + "!", word + "@2023"]
    mutations.append(word * 2)
    mutations.append(word.capitalize() + word.upper())
    mutations.append(''.join(random.choice((str.upper, str.lower))(c) for c in word))
    return mutations

# Zapisuje listę haseł do pliku
def save_to_file(word_list, filename):
    with open(filename, 'w') as file:
        for word in word_list:
            file.write(word + '\n')
    print(f"Wyniki zapisane do {filename}")

# Testowanie funkcji
url = 'https://en.wikipedia.org/wiki/Warsaw_University_of_Technology'
all_words = get_all_words_from(url)
occurrences = count_occurrences_in(all_words)

# Przykład generowania mutacji i zapisu do pliku
top_word = occurrences[0][0]
mutations = generate_password_mutations(top_word)
save_to_file(mutations, "wordlist.txt")
```

---

## Skrypt do łamania hashy

Poniższy skrypt można wykorzystać do porównywania wygenerowanych hashy SHA-256 z hashami przechowywanymi w pliku `hash.txt`.

```python
import hashlib

# Pliki do przetworzenia
wordlist_file = 'wordlist.txt'
hash_file = 'hash.txt'

# Wczytaj hashe z pliku hash.txt do zbioru dla szybszego sprawdzania
with open(hash_file, 'r') as f:
    target_hashes = {line.strip() for line in f}

# Funkcja do generowania SHA-256 dla danego słowa
def sha256_hash(word):
    return hashlib.sha256(word.encode()).hexdigest()

# Przetwarzanie słownika i porównanie hashy
with open(wordlist_file, 'r') as f:
    for word in f:
        word = word.strip()
        hashed_word = sha256_hash(word)
        
        if hashed_word in target_hashes:
            print(f"Dopasowanie znalezione: {word} -> {hashed_word}")
```

### Instrukcja użycia skryptu

1. **Przygotowanie katalogu roboczego**:
   - Utworzenie nowego katalogu do pracy. W terminalu:
     ```
     mkdir hash_cracker
     cd hash_cracker
     ```
   - Umieszczenie w katalogu dwóch plików:
     - `wordlist.txt` – plik z wygenerowaną listą słów (wordlistą).
     - `hash.txt` – plik zawierający hashe do złamania (po jednym hashu w każdej linii).

2. **Zapisanie skryptu**:
   - Skopiowanie kodu skryptu powyżej i zapisanie go w pliku `hash_cracker.py`.

3. **Uruchomienie skryptu**:
   - W terminalu, będąc w katalogu `hash_cracker`, uruchomienie skryptu:
     ```
     python3 hash_cracker.py
     ```
   - Skrypt przetwarza każdą linię w pliku `wordlist.txt`, generuje hashe dla każdego słowa i porównuje je z hashami w pliku `hash.txt`.
   - Dopasowanie wyświetli się w formacie:
     ```
     Dopasowanie znalezione: <słowo> -> <hash>
     ```
4. **Wynik**:
   - Po zakończeniu działania skryptu w terminalu wyświetlą się pasujące hasła do hashy w `hash.txt`. Skrypt zakończy działanie po przetworzeniu całej `wordlist.txt`.

---

### Wskazówki

Aby uzyskać hasła zbliżone do podanych przykładów, warto zastosować następujące techniki i strategie:

1. **Analiza i tematyczne dopasowanie słów**: Skrypt powinien analizować kontekst strony internetowej, aby zidentyfikować słowa kluczowe związane z osobą, postacią historyczną lub popularnym terminem, np. „Leonardo”, „Einstein”, „Curie”. Pozwoli to na tworzenie haseł powiązanych z charakterystycznymi atrybutami, zawodami lub znanymi dokonaniami postaci.

2. **Ograniczenie minimalnej długości słowa**: Aby uniknąć zbędnych i krótkich słów, które rzadko są używane jako hasła, skrypt powinien filtrować słowa krótsze niż 5 znaków.

3. **Łączenie najczęściej występujących słów**:
   - Skrypt powinien analizować, które słowa najczęściej występują na stronie, i łączyć je w pary lub ciągi znaków, np. „securitypassword”, „passwordsecurity”.
   - Tego rodzaju kombinacje można również tworzyć dla popularnych terminów, np. „CurieScience”, „NewtonLaws”.

4. **Generowanie mutacji haseł**:
   - **Zamiana liter na symbole**: Używanie popularnych zamienników dla liter, takich jak:
     - „a” ➔ „@”
     - „s” ➔ „$”
     - „o” ➔ „0”
     - „e” ➔ „3”
     - „i” ➔ „1”
     - „t” ➔ „7”
   - **Losowe mieszanie wielkości liter**: Przypadkowe łączenie wielkich i małych liter, aby symulować często stosowane techniki, np. „AlB3RtEinStEin”.
   - **Dodawanie zakończeń**: Do każdego słowa lub nazwiska dodaj liczby i symbole, np.:
     - „123”, „01”, „99”, „999”, „!”, „!!!”, „@2023” lub „2023”, „_”, „*”
   - **Same symbole na końcu słowa**: Na końcu hasła dodaj jeden lub dwa symbole, jak „*”, „#”, „@”, „$”, "##", "#@" itp. (np. „AlB3RtEinStEin@@”)


