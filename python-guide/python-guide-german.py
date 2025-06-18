# Lernhilfe Python - Alex

# - Eine Zeile nach der anderen wird ausgeführt.
# - Kommentare werden mit einem # am Anfang der Zeile geschrieben. (Werden von python ignoriert)

# ---------------- Datentypen

# Es gibt verschiedene Datentypen in Python

# Integer (Ganzzahl)
5

# String (Text)
"Hello World!"
"123" # Das ist auch ein String, weil es in "" steht, auch wenn es nur Zahlen sind
# Mit Strings kann man nicht rechnen.

# Float (Kommazahl)
3.14

# Boolean (True oder False)
True
False

# ---------------- Variablen umwandeln

# Beispiele:
int(x) # Umwandeln in Integer (Ganzzahl)
str(x) # Umwandeln in String (Text)
float(x)  # Umwandeln in Float (Kommazahl)

alter = "17" # String (Text)
alter_zahl = int(alter) # Umwandeln in Integer (Ganzzahl)

# ---------------- variabeln zuweisen

# Man kann variabeln erstellen und ihnen Werte zuweisen. Man kann sie nennen wie man möchte, aber es ist gut, wenn der Name mit ihrem Inhalt zu tun hat.
a = 5 # Integer (Ganzzahl)
b = 10
name = "Alex" # String (Text), muss "" oder '' haben

# Rechnen mit Variablen:

# Operatoren:
# +  Addition
# -  Subtraktion
# *  Multiplikation
# /  Division
# %  Modulo (Rest bei Division)

c = a + b # c wird 15 sein, weil 5 + 10 = 15
a = a + 1 # a wird um 1 erhöht, also a = 6

# ---------------- Konsole aus-/eingabe

print("Hallo Welt!") # Gibt "Hallo Welt!" in der Konsole aus

# User input:
print("Wie heisst du?: ")
name = input() # Der User muss in die Konsole etwas eingeben, was dann in der Variable 'name' gespeichert wird
# Abkürzung:
name = input("Wie heisst du?: ")


# ---------------- if-else # Bedingungen

# Es schaut zuerst die Bedingung von 'if' an, wenn die Bedingung wahr ist, wird der Codeblock darunter ausgeführt, wenn nicht, wird die nächste 'elif' Bedingung geprüft, und wenn keine der Bedingungen wahr ist, wird der 'else' Block ausgeführt.
# Man muss immer tab drücken, um einzurücken

if a < b: # Wenn a kleiner als b ist
    print("a ist kleiner als b")
elif a == b: # Wenn a gleich b ist # WICHTIG: '==' ist der Vergleichsoperator, '=' ist der Zuweisungsoperator, anders als in Mathe!
    print("a ist gleich b")
else: # Wenn keine der vorherigen Bedingungen zutrifft
    print("a ist größer als b")

# ---------------- Schleifen
# Es gibt 2 Arten von Schleifen: 'for' und 'while'
# 'for' Schleife: wird für eine bestimmte Anzahl von Iterationen verwendet:
fruits = ["Apfel", "Banane", "Kirsche"]
for fruit in fruits: # 'fruit' ist die temporäre Variable, die für jedes Element im Array 'fruits' verwendet wird
    print(fruit) # gibt jeden Wert des Arrays aus (Apfel, Banane, Kirsche)

# 'while' Schleife: wird verwendet, solange eine Bedingung wahr ist:
a = 0
b = 5
while a < b: # Solange a kleiner als b ist
    print("a ist kleiner als b")
    a = a + 1 # Erhöht a um 1, damit die Schleife irgendwann endet, sonst wäre es eine Endlosschleife

# Um eine Endlosschleife zu machen, kann man 'while True:' schreiben

# ---------------- Input von dem User bekommen

print("Bitte geben Sie Ihren Namen ein:")
name = input()
# MACH DAS GLEICHE WIE:
name = input("Bitte geben Sie Ihren Namen ein:")
# Wichtig: input() gibt immer einen String zurück! Wenn du eine Zahl (intiger) davon kriegen willst, machst du z.B. zahl = int(input("Gib eine Zahl ein: "))

# ---------------- String interpolation (variabeln in strings(text) einfügen):
# Es gibt 2 varianten

print("Hallo " + name + ", willkommen!") # das '+' verbindet Strings
print(f"Hallo {name}, willkommen!") # das 'f' am Anfang muss man hinzufügen, um variabeln mit {} einfügen zu können

# Wenn die variable eine Zahl ist, muss man sie zuerst in eine 'String' konvertieren:
age = 17
print("Ich bin " + str(age) + " Jahre alt.")
print(f"Ich bin {age} Jahre alt.") # das 'f' am Anfang muss man hinzufügen, um variabeln mit {} einfügen zu können

# ---------------- Arrays

# Anstatt nur eine Variable mit einem Wert, kann man einen Array mit einer liste von Werten definieren:

fruits = ["Apfel", "Banane", "Kirsche"]
print(fruits[0]) # gibt den ersten Wert des Arrays aus (Man zählt ab 0) (Apfel)
print(fruits[1]) # gibt den zweiten Wert des Arrays aus (Banane)

new_fruit = "Orange"
fruits.append(new_fruit) # Fügt 'Orange' zum Array 'fruits' hinzu
# ["Apfel", "Banane", "Kirsche", "Orange"]



# um etwas zum beispiel 10 mal zu machen:
for i in range(10):
    #...
# 'range(10)' würde einen Array mit den Werten 0 bis 9 erstellen ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).

# ---------------- module

# Module kann man importieren, um zusätzliche Funktionen zu nutzen
# Beispiele:

import random
zufall_zahl = random.randint(1, 10) # Gibt eine zufällige Zahl zwischen 1 und 10 zurück

fruits = ["Apfel", "Banane", "Kirsche"]
zufall_frucht = random.choice(fruits) # Gibt eine zufällige Frucht aus dem Array 'fruits' zurück
print(zufall_frucht) # "Kirsche" oder "Banane" oder "Apfel"


# ---------------- Funktionen

# Man kann eigene Funktionen erstellen, um wiederholende Logik zu kapseln und den Code übersichtlicher zu machen.
def begruessung(name): # Funktion mit einem Parameter 'name'
    print(f"Hallo {name}, willkommen!") # Gibt eine Begrüßung aus

name = input("Wie heisst du?: ")
begruessung(name) # Ruft die Funktion 'begruessung' mit dem Parameter 'name' auf


def summe(zahl_eins, zahl_zwei): # Funktion mit 2 Parametern 'zahl_eins' und 'zahl_zwei'
    return zahl_eins + zahl_zwei # Gibt die Summe von zahl_eins und zahl_zwei zurück

a = 5
b = 10
resultat = summe(a, b) # a füllt den Parameter 'zahl_eins' und b füllt den Parameter 'zahl_zwei'
print(f"Die Summe von {a} und {b} ist {resultat}.") # Gibt die Summe von a und b aus

# ---------------- Hangman Beispiel mit Erklärung
#####################
import random

words = ["python", "java", "javascript", "html", "css"] # Liste von Wörtern (Array)
word = random.choice(words) # Züfälliges Wort auswählen
guessed_letters = [] # Liste für bereits geratene Buchstaben
anzeige = "" # String für die Anzeige initialisieren
print(f"Das Wort hat {len(word)} Buchstaben.") # len() gibt die Länge an
for i in range(len(word)): # "for i in range(x)" macht, dass die for Schleife so viel mal iteriert wie x
    anzeige += "_ "
    print(anzeige)
    guess = input("Bitte geben Sie einen Buchstaben ein: ")
    if len(guess) != 1:
        print("Bitte geben Sie nur einen Buchstaben ein.")
        continue
    guessed_letters.append(guess) # Füge geratenen Buchstaben zur Liste hinzu
    if guess in word: # schaut ob der Buchstabe im Wort ist
        continue
    if guess in word: # schaut ob der Buchstabe im Wort ist
        print(f"Der Buchstabe {guess} ist im Wort.")
        anzeige = ""
        for letter in word:
            if letter in guessed_letters:
                anzeige += letter + " "
            else:
                anzeige += "_ "
        print(anzeige)
    else:
        print(f"Der Buchstabe {guess} ist nicht im Wort.")
#####################



# Meine Beispiellösungen zu manchen der schwierigen Aufgaben:
# https://github.com/Alex7k/simple-python-scripts/tree/main/python