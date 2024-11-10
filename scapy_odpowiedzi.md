## Odpowiedzi do zadań - scapy

### Krok 1: Wysłanie pakietu ICMP do localhost
```python
def send_ping():
    packet = IP(dst="127.0.0.1") / ICMP()
    reply = sr1(packet, timeout=1, verbose=False)
    if reply:
        print(f"Otrzymano odpowiedź od {reply.src}")
    else:
        print("Brak odpowiedzi!")
```

---

### Krok 2: Analiza pakietu odpowiedzi
```python
def analyze_ping():
    packet = IP(dst="127.0.0.1") / ICMP()
    reply = sr1(packet, timeout=1, verbose=False)
    if reply:
        print("Odpowiedź:")
        print(reply.show())
    else:
        print("Brak odpowiedzi!")
```

---

### Krok 3: Rozszerzenie funkcji
```python
def extended_ping():
    packet = IP(dst="127.0.0.1") / ICMP()
    reply = sr1(packet, timeout=1, verbose=False)
    if reply:
        ttl = reply[IP].ttl
        print(f"Otrzymano odpowiedź od {reply.src} z TTL={ttl}")
        if ttl > 1:
            print("Pakiet dotarł do hosta.")
        else:
            print("Pakiet prawdopodobnie został zatrzymany po drodze.")
    else:
        print("Brak odpowiedzi!")
```

### Uruchomienie całości

```python
from scapy.all import *

# tu zdefiniowane powyżej funkcje...

print("Krok 1: Wysłanie pakietu ICMP do localhost")
send_ping()
print("\nKrok 2: Analiza pakietu odpowiedzi")
analyze_ping()
print("\nKrok 3: Rozszerzenie funkcji")
extended_ping()
```

---

## Zadanie dodatkowe

```python
import time
from scapy.all import *

def extended_ping_with_rtt(ip, count=4):
    results = []  # Lista do przechowywania wyników

    for i in range(count):
        packet = IP(dst=ip) / ICMP()
        start_time = time.time()  # Start licznika czasu
        reply = sr1(packet, timeout=1, verbose=False)
        end_time = time.time()  # Koniec licznika czasu

        if reply:
            ttl = reply[IP].ttl
            rtt = (end_time - start_time) * 1000  # RTT w milisekundach
            reachable = ttl > 1
            results.append({
                "ip": reply.src,
                "ttl": ttl,
                "rtt": round(rtt, 2),
                "reachable": reachable
            })
        else:
            results.append({
                "ip": ip,
                "ttl": None,
                "rtt": None,
                "reachable": False
            })

    # Podsumowanie wyników
    print(f"Podsumowanie ping dla {ip}:")
    for res in results:
        if res["reachable"]:
            print(f"Host: {res['ip']}, TTL: {res['ttl']}, RTT: {res['rtt']} ms, Status: Osiągalny")
        else:
            print(f"Host: {res['ip']}, Status: Nieosiągalny")

# Przykład użycia
extended_ping_with_rtt("127.0.0.1")
```
