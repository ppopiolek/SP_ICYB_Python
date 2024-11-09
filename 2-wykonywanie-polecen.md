## Ćwiczenia do wykonania

1. Napisz skrypt, w którym zdefiniujesz dwie liczby, a następnie z wykorzystaniem funkcji print wypisz ich sumę. Kod wykonaj z pliku.
2. Zrób to samo tylko przy wykorzystaniu Python IDLE.
3. Zapisz i wykonaj z pliku następujący skrypt w którym odwołanie do zmiennej następuje przed jej zadeklarowaniem, sprawdź co się stanie. Następnie popraw skrypt, tak aby wszystko wykonało się prawidłowo.
    ```python
    print(tekst)
    tekst = "Od góry do dołu"
    ```

### Przykładowe rozwiązania

#### Zadanie 1.
```python
liczba1 = 2
liczba2 = 4
print(liczba1 + liczba2)
```
```
$ python3 skrypt.py
6
```

#### Zadanie 2.
```
$ python3 
...
>>> liczba1 = 2
>>> liczba2 = 4
>>> liczba1 + liczba2
6
```

#### Zadanie 3. 
```python
tekst = "Od góry do dołu"
print(tekst)
```
```
Od góry do dołu
```