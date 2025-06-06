# https://en.wikipedia.org/wiki/Collatz_conjecture

# Even number: / 2
# Odd number: * 3 + 1

samples = 100000
leaderboard = []
for startingnumber in range(1, samples):
  # measure how many steps to end up in the 4, 2, 1 loop
  step = 0
  highestnumber = startingnumber
  number = startingnumber
  while True:
    step += 1
    if number % 2 == 0:
      number = number // 2
    elif number % 2 == 1:
      number = number * 3 + 1
    if number > highestnumber:
      highestnumber = number
    # print(number)
    if number == 1:
      # print(f"{startingnumber} arrived at loop at step {step} with highest number being {highestnumber}")
      leaderboard.append([startingnumber, step, highestnumber])
      break

print("Leaderboard:")
print("Starting number, achieved step, highest number")
leaderboard.sort(key=lambda x: x[2], reverse=True)
leaderboardlength = len(leaderboard)
if 10 < leaderboardlength:
  leaderboardlength = 10
for i in range(leaderboardlength):
  print(leaderboard[i])
