# Caesar cipher

## - Parameters -

word = "Hello, world!".lower()
shift = 6

## --

alphabet = list("abcdefghijklmnopqrstuvwxyz")

letters = list((word).lower())

def cipher(letter,shift):
  for i in range(len(alphabet)):
    if letter == alphabet[i]:
      return alphabet[(i+shift) % len(alphabet)]
  return letter # letter not in alphabet, leave unchanged
  exit()

newWord = ""
for letter in letters:
  newWord += cipher(letter,shift)

print(f"'{word}' caesar shifted by {shift} turns to '{newWord}'")
