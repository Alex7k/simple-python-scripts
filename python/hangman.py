import random

wordlist = [ "apple", "banana", "burger", "equilibrium", "operator", "keyboard", "paragraph", "obituary", "technology", "optimal" ]
word = random.choice(wordlist)

temp = []
for i in range(len(word)):
  temp.append("_ ")

guessedletters = []

while True:
  print(" ".join(temp))
  print("Guessed letters: "+", ".join(guessedletters))
  if temp == list(word):
    print(f"You won with {len(guessedletters)} tries!")
    exit()
  userinput = input("Guess a letter: ")
  if len(userinput) != 1:
    print("Invalid letter!")
    continue
  if userinput in guessedletters:
    print("You've already guessed that letter!")
    continue
  else:
    guessedletters.append(userinput)
    for i in range(len(word)):
      if userinput == word[i]:
        temp[i] = word[i]