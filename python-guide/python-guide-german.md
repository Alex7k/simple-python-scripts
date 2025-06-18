# Lernhilfe Python

- Eine Zeile nach der anderen wird ausgeführt.
- Kommentare werden mit einem `#` am Anfang der Zeile geschrieben. (Werden von Python ignoriert)

---

## Datentypen

Es gibt verschiedene Datentypen in Python:

- **Integer (Ganzzahl)**

    ```python
    5
    ```

- **String (Text)**

    ```python
    "Hello World!"
    "123" # Das ist auch ein String, weil es in "" steht, auch wenn es nur Zahlen sind
    # Mit Strings kann man nicht rechnen.
    ```

- **Float (Kommazahl)**

    ```python
    3.14
    ```

- **Boolean (True oder False)**

    ```python
    True
    False
    ```

---

## Variablen umwandeln

Beispiele:

```python
int(x)   # Umwandeln in Integer (Ganzzahl)
str(x)   # Umwandeln in String (Text)
float(x) # Umwandeln in Float (Kommazahl)

alter = "17" # String (Text)
alter_zahl = int(alter) # Umwandeln in Integer (Ganzzahl)
```

---

## Variablen zuweisen

Man kann Variablen erstellen und ihnen Werte zuweisen. Man kann sie nennen wie man möchte, aber es ist gut, wenn der Name mit ihrem Inhalt zu tun hat.

```python
a = 5 # Integer (Ganzzahl)
b = 10
name = "Alex" # String (Text), muss "" oder '' haben
```

### Rechnen mit Variablen

Operatoren:

- `+`  Addition
- `-`  Subtraktion
- `*`  Multiplikation
- `/`  Division
- `%`  Modulo (Rest bei Division)

```python
c = a + b # c wird 15 sein, weil 5 + 10 = 15
a = a + 1 # a wird um 1 erhöht, also a = 6
```

---

## Konsole aus-/eingabe

```python
print("Hallo Welt!") # Gibt "Hallo Welt!" in der Konsole aus
```

### User input

```python
print("Wie heisst du?: ")
name = input() # Der User muss in die Konsole etwas eingeben, was dann in der Variable 'name' gespeichert wird
# Abkürzung:
name = input("Wie heisst du?: ")
```

---

## if-else (Bedingungen)

Es schaut zuerst die Bedingung von `if` an, wenn die Bedingung wahr ist, wird der Codeblock darunter ausgeführt, wenn nicht, wird die nächste `elif` Bedingung geprüft, und wenn keine der Bedingungen wahr ist, wird der `else` Block ausgeführt.

Man muss immer Tab drücken, um einzurücken.

```python
if a < b: # Wenn a kleiner als b ist
    print("a ist kleiner als b")
elif a == b: # Wenn a gleich b ist
    print("a ist gleich b")
else: # Wenn keine der vorherigen Bedingungen zutrifft
    print("a ist größer als b")
```

---

## Schleifen

Es gibt 2 Arten von Schleifen: `for` und `while`

### for-Schleife

Wird für eine bestimmte Anzahl von Iterationen verwendet:

```python
fruits = ["Apfel", "Banane", "Kirsche"]
for fruit in fruits: # 'fruit' ist die temporäre Variable, die für jedes Element im Array 'fruits' verwendet wird
    print(fruit) # gibt jeden Wert des Arrays aus (Apfel, Banane, Kirsche)
```

### while-Schleife

Wird verwendet, solange eine Bedingung wahr ist:

```python
a = 0
b = 5
while a < b: # Solange a kleiner als b ist
    print("a ist kleiner als b")
    a = a + 1 # Erhöht a um 1, damit die Schleife irgendwann endet, sonst wäre es eine Endlosschleife
```

Um eine Endlosschleife zu machen, kann man `while True:` schreiben.

---

## Input von dem User bekommen

```python
print("Bitte geben Sie Ihren Namen ein:")
name = input()
# MACH DAS GLEICHE WIE:
name = input("Bitte geben Sie Ihren Namen ein:")
# Wichtig: input() gibt immer einen String zurück! Wenn du eine Zahl (Integer) davon kriegen willst, machst du z.B.:
zahl = int(input("Gib eine Zahl ein: "))
```

---

## String Interpolation (Variablen in Strings/Text einfügen)

Es gibt 2 Varianten:

```python
print("Hallo " + name + ", willkommen!") # das '+' verbindet Strings
print(f"Hallo {name}, willkommen!") # das 'f' am Anfang muss man hinzufügen, um Variablen mit {} einfügen zu können
```

Wenn die Variable eine Zahl ist, muss man sie zuerst in einen String konvertieren:

```python
age = 17
print("Ich bin " + str(age) + " Jahre alt.")
print(f"Ich bin {age} Jahre alt.") # das 'f' am Anfang muss man hinzufügen, um Variablen mit {} einfügen zu können
```

---

## Arrays

Anstatt nur eine Variable mit einem Wert, kann man ein Array mit einer Liste von Werten definieren:

```python
fruits = ["Apfel", "Banane", "Kirsche"]
print(fruits[0]) # gibt den ersten Wert des Arrays aus (Man zählt ab 0) (Apfel)
print(fruits[1]) # gibt den zweiten Wert des Arrays aus (Banane)

new_fruit = "Orange"
fruits.append(new_fruit) # Fügt 'Orange' zum Array 'fruits' hinzu
# ["Apfel", "Banane", "Kirsche", "Orange"]
```

Um etwas zum Beispiel 10 mal zu machen:

```python
for i in range(10):
    # ...
# 'range(10)' würde einen Array mit den Werten 0 bis 9 erstellen ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).
```

---

## Module

Module kann man importieren, um zusätzliche Funktionen zu nutzen.

Beispiele:

```python
import random
zufall_zahl = random.randint(1, 10) # Gibt eine zufällige Zahl zwischen 1 und 10 zurück

fruits = ["Apfel", "Banane", "Kirsche"]
zufall_frucht = random.choice(fruits) # Gibt eine zufällige Frucht aus dem Array 'fruits' zurück
print(zufall_frucht) # "Kirsche" oder "Banane" oder "Apfel"
```

---

## Funktionen

Man kann eigene Funktionen erstellen, um wiederholende Logik zu kapseln und den Code übersichtlicher zu machen.

```python
def begruessung(name): # Funktion mit einem Parameter 'name'
    print(f"Hallo {name}, willkommen!") # Gibt eine Begrüßung aus

name = input("Wie heisst du?: ")
begruessung(name) # Ruft die Funktion 'begruessung' mit dem Parameter 'name' auf

# ---
def summe(zahl_eins, zahl_zwei): # Funktion mit 2 Parametern 'zahl_eins' und 'zahl_zwei'
    return zahl_eins + zahl_zwei # Gibt die Summe von zahl_eins und zahl_zwei zurück

a = 5
b = 10
resultat = summe(a, b) # a füllt den Parameter 'zahl_eins' und b füllt den Parameter 'zahl_zwei'
print(f"Die Summe von {a} und {b} ist {resultat}.") # Gibt die Summe von a und b aus
```

---

## Meine Beispiellösungen zu manchen der schwierigen Aufgaben

[https://github.com/Alex7k/simple-python-scripts/tree/main/python](https://github.com/Alex7k/simple-python-scripts/tree/main/python)
