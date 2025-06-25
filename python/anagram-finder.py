dict = [
  'apple',
  'banana',
  'cherry',
  'date',
  'earth',
  'heart',
  'rathe',
  'fried',
  'fired'
]

input_word = "fried"

anagrams = []
for word in dict:
  if len(input_word) == len(word) and input_word != word:
    print(word)
    if sorted(list(input_word)) == sorted(list(word)):
      anagrams.append(word)

print(f"Anagrams to '{input_word}':")
print(anagrams)