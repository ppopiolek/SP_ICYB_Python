# Instrukcja: Podstawy Scapy z zadaniem do wykonania

---

## Wprowadzenie do Scapy

Scapy to potężne narzędzie do manipulowania i analizowania pakietów sieciowych. Umożliwia tworzenie, wysyłanie, odbieranie i modyfikowanie pakietów na różnych poziomach protokołów sieciowych.

---

### Instalacja

1. Upewnij się, że masz zainstalowanego Pythona (najlepiej wersję 3.x).
2. Zainstaluj Scapy za pomocą pip:
   ```bash
   pip install scapy
   ```

---

### Podstawowe funkcje

#### 1. Importowanie Scapy
Przed użyciem należy zaimportować bibliotekę:
```python
from scapy.all import *
```

#### 2. Tworzenie pakietów
Scapy umożliwia tworzenie pakietów dla różnych protokołów:
- **Ethernet (warstwa 2)**:
  ```python
  eth = Ether()
  print(eth.show())
  ```
  
  ```
  ###[ Ethernet ]###
  dst       = ff:ff:ff:ff:ff:ff
  src       = 00:00:00:00:00:00
  type      = 0x9000
  ```

- **IP (warstwa 3)**:
  ```python
  ip = IP(dst="127.0.0.1")
  print(ip.show())
  ```
  
  ```
  ###[ IP ]###
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     =
  frag      = 0
  ttl       = 64
  proto     = hopopt
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.0.0.1
  ```

#### 3. Łączenie warstw
Warstwy można łączyć, tworząc bardziej złożone pakiety:
```python
packet = IP(dst="127.0.0.1") / ICMP()
print(packet.show())
```

```
###[ IP ]###
  version   = 4
  ...
  dst       = 127.0.0.1
###[ ICMP ]###
  type      = echo-request
  code      = 0
  chksum    = None
  id        = 0x0
  seq       = 0x0
```

#### 4. Wysyłanie pakietów
Scapy umożliwia wysyłanie pakietów do lokalnego hosta:
```python
send(IP(dst="127.0.0.1") / ICMP())
```
```
.
Sent 1 packets.
```

---

## Zadanie praktyczne

### Cel:
Stwórz i prześlij pakiet IP/ICMP, a następnie odczytaj jego szczegóły oraz zinterpretuj odpowiedź.

---

### Instrukcje

#### Krok 1: Wysłanie pakietu ICMP do localhost
Stwórz funkcję, która:
1. Tworzy pakiet IP/ICMP z adresem docelowym `127.0.0.1`.
2. Wysyła pakiet i odbiera odpowiedź.

**Podpowiedź:**
```python
def send_ping():
    # Stwórz pakiet IP/ICMP
    # Wyślij pakiet i odbierz odpowiedź
    # Jeśli odpowiedź jest dostępna, wypisz adres źródłowy
    # W przeciwnym razie wypisz, że brak odpowiedzi
```

---

#### Krok 2: Analiza pakietu odpowiedzi
Dodaj analizę pakietu zwrotnego, aby odczytać szczegóły odpowiedzi.

**Podpowiedź:**
```python
def analyze_ping():
    # Stwórz pakiet IP/ICMP
    # Wyślij pakiet i odbierz odpowiedź
    # Jeśli odpowiedź jest dostępna, użyj .show() na pakiecie, aby wypisać szczegóły
    # W przeciwnym razie wypisz, że brak odpowiedzi
```

---

#### Krok 3: Rozszerzenie funkcji
Rozszerz funkcję, aby:
1. Wyświetlić wartość TTL (Time-to-Live) z odpowiedzi ICMP.
2. Zinterpretować, czy pakiet dotarł do docelowego hosta (TTL ≥ 1).

**Podpowiedź:**
```python
def extended_ping():
    # Stwórz pakiet IP/ICMP
    # Wyślij pakiet i odbierz odpowiedź
    # Jeśli odpowiedź jest dostępna:
        # Pobierz TTL z warstwy IP
        # Wypisz TTL oraz interpretację (czy dotarło do hosta)
    # W przeciwnym razie wypisz, że brak odpowiedzi
```

---

#### Zadanie dodatkowe: Rozbudowana analiza i raportowanie

Rozszerz funkcję `extended_ping` o następujące funkcjonalności:

1. **Licznik czasu odpowiedzi**: Zmierz czas odpowiedzi dla każdego pakietu (RTT - Round-Trip Time).
2. **Zapisywanie wyników**: Zapisz wyniki do listy w postaci słownika, zawierającego:
   - Adres IP docelowy.
   - TTL odpowiedzi.
   - Czas odpowiedzi (RTT) w milisekundach.
   - Informację, czy pakiet dotarł do hosta.
3. **Wypisanie podsumowania**: Po zakończeniu działania funkcji wypisz wszystkie zapisane wyniki w czytelnym formacie.

**Podpowiedzi:**
1. Użyj modułu `time` do zmierzenia czasu odpowiedzi.
2. Sformatuj dane wyniku w postaci listy słowników, np.:
   ```python
   results = [
       {"ip": "127.0.0.1", "ttl": 64, "rtt": 2.34, "reachable": True},
       ...
   ]

Polecane źródło: https://www.freecodecamp.org/news/how-to-use-scapy-python-networking/
