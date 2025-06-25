# Caesar cipher

## - Parameters -

word = "hello".lower()
shift = 6

## --

alphabet = list("abcdefghijklmnopqrstuvwxyz")

letters = list((word).lower())

def cipher(letter,shift):
  for i in range(len(alphabet)):
    if letter == alphabet[i]:
      return alphabet[(i+shift) % len(alphabet)]
  print("Not all symbols included in alphabet! Aborting...")
  exit()

newWord = ""
for letter in letters:
  newWord += cipher(letter,shift)

print(f"'{word}' caesar shifted by {shift} turns to '{newWord}'")