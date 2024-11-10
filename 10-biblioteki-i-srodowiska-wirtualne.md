## Ćwiczenia do wykonania

1. Rozpocznij od zainstalowania biblioteki `click` i przy jej pomocy stwórz prosty program, który poprosi użytkownika o wprowadzenie swojego imienia i wyświetli personalizowane powitanie (znajdź i sprawdź dokumentację biblioteki).
2. Stwórz wirtualne środowisko za pomocą `venv`, zainstaluj w nim pakiet `numpy`, a następnie wygeneruj plik `requirements.txt`. Podejrzyj wygenerowany plik.
3. Użyj Conda do stworzenia nowego środowiska, zainstaluj w nim pakiet `numpy` i wyeksportuj listę pakietów do pliku `environment.yml`. Podejrzyj wygenerowany plik.
4. Wykorzystaj biblioteki `requests` i `BeautifulSoup` do pobrania i wyświetlenia tytułu strony internetowej. Zainstaluj wymagane pakiety, jeśli nie są jeszcze zainstalowane. Znajdź i skorzystaj z ogólnodostępnej dokumentacji wskazanych bibliotek.

### Przykładowe rozwiązania


#### Zadanie 1.
```python
import click

@click.command()
def welcome():
    name = click.prompt('Proszę wpisz swoje imię')
    click.echo(f'Witaj, {name}!')

if __name__ == "__main__":
    welcome()
```

```
$ python welcome.py
Proszę wpisz swoje imię: Marek
Witaj, Marek!
```
#### Zadanie 2.
```bash
# Tworzenie wirtualnego środowiska
python -m venv myenv
# Aktywacja środowiska w systemie Unix/macOS
source myenv/bin/activate 
# Aktywacja środowiska w systemie Windows
myenv\Scripts\activate
# Instalacja pakietów
pip install requests
# Generowanie pliku requirements.txt
pip freeze > requirements.txt
```

```
$ cat requirements.txt
requests==x.x.x    <-- tu będzie konkretna wersja
```

#### Zadanie 3.
```bash
# Tworzenie nowego środowiska Conda
conda create --name mycondaenv
# Aktywowanie środowiska
conda activate mycondaenv
# Instalacja pakietu numpy
conda install numpy
# Eksportowanie listy pakietów do pliku
conda env export > environment.yml
```

```
$ cat environment.yml
name: mycondaenv
dependencies:
  - numpy=x.x.x
  - pip:
    - some-package==x.x.x
```

#### Zadanie 4.
```python
import requests
from bs4 import BeautifulSoup

# Przykładowy URL do pobrania danych
url = 'https://www.example.com'

# Pobranie danych ze strony
response = requests.get(url)

# Utworzenie obiektu BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Wyszukanie tytułu i wyświetlenie go
title = soup.find('title').text
print(f'Tytuł strony: {title}')
```

```
Tytuł strony: Example Domain
```
