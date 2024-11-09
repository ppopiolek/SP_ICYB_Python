## Ćwiczenia do Wykonania

1. Jesteś administratorem systemu i masz za zadanie zaktualizować listę protokołów sieciowych używanych w firmie. Obecna lista protokołów zawiera `["HTTP", "FTP", "SSH", "TELNET"]`. Twoim zadaniem jest usunięcie przestarzałego protokołu "TELNET", dodanie bezpieczniejszego "HTTPS". Na koniec, wyświetl dwa najnowsze protokoły dodane do listy.
2. W działaniach związanych z cyberbezpieczeństwem ważne jest, aby hasła były skomplikowane i trudne do odgadnięcia. Posiadasz hasło `"aB3$7@xZ"`, które chcesz zbadać pod kątem złożoności. Twoim zadaniem jest sprawdzenie, które znaki są alfanumeryczne, a następnie przekształcenie hasła na format, w którym wszystkie litery są wielkie, aby zasymulować wymóg użycia wielkich liter w hasłach. Na koniec odwróć kolejność znaków, aby zobaczyć, jak hasło wyglądałoby w mniej przewidywalnej formie.
3. Masz dany słownik raport, który zawiera informacje o stanie zabezpieczeń różnych usług sieciowych. Twoim zadaniem jest zaktualizowanie tego słownika, aby każda usługa była zmapowana na status "bezpieczny" lub "niebezpieczny". Po zaktualizowaniu słownika, wyświetl status bezpieczeństwa dla usługi "FTP" oraz "SSH". W słowniku raport powinny znaleźć się również usługi "SMTP", "DNS" oraz "HTTPS", gdzie "SMTP" i "DNS" powinny mieć przypisany status "niebezpieczny", a "HTTPS" status "bezpieczny".

### Przykładowe Rozwiązania

#### Zadanie 1.
```python
# Definiujemy listę protokołów
protokoly = ["HTTP", "FTP", "SSH", "TELNET"]

# Aktualizacja listy protokołów
protokoly.remove("TELNET")
protokoly.append("HTTPS")


# Wyświetlanie dwóch ostatnich protokołów
print("\nDwa ostatnie protokoły w liście:")
print(protokoly[-2:])
```

```
Dwa ostatnie protokoły w liście:
['SSH', 'HTTPS']
```

#### Zadanie 2.
```python
# Definiujemy hasło
haslo = "aB3$7@xZ"

# Znaki alfanumeryczne
alfanumeryczne = ''.join([znak for znak in haslo if znak.isalnum()])

# Wersja hasła z wielkimi literami
haslo_wielkie = haslo.upper()

# Hasło w odwróconej kolejności
haslo_odwrocone = haslo[::-1]

# Wyniki
print("Znaki alfanumeryczne:", alfanumeryczne)
print("Hasło z wielkimi literami:", haslo_wielkie)
print("Hasło odwrócone:", haslo_odwrocone)
```

```
Znaki alfanumeryczne: aB37xZ
Hasło z wielkimi literami: AB3$7@XZ
Hasło odwrócone: Zx@7$3Ba
```

#### Zadanie 3.
```python
# Słownik raport z rozbudowanym stanem bezpieczeństwa usług
raport = {
    "SSH": "bezpieczny",
    "FTP": "niebezpieczny",
    "HTTP": "bezpieczny",
    "SMTP": "niebezpieczny",
    "DNS": "bezpieczny",
    "HTTPS": "bezpieczny"
}

# Wyświetlenie statusu dla usługi FTP
print("Status bezpieczeństwa dla FTP:", raport["FTP"])

# Wyświetlenie statusu dla usługi SSH
print("Status bezpieczeństwa dla SSH:", raport["SSH"])

```

```
Status bezpieczeństwa dla FTP: niebezpieczny
Status bezpieczeństwa dla SSH: bezpieczny
```