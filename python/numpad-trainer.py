import random
import time

print("Welcome to the Numpad Trainer. Type 'exit' to quit")

while True:
  number = random.randint(1,9999999)
  print("To type: " + str(number))
  start_time = time.time()
  user_input = input("-------> ")
  end_time = time.time()
  if user_input == "exit":
    exit()
  if str(number) != user_input:
    print("You made a mistake!")
  else:
    elapsed = end_time - start_time
    if not 'highscore' in locals():
      highscore = elapsed
    else:
      highscore = min([elapsed, highscore])
    print(f"{elapsed:.2f}s - highscore: {highscore:.2f}s")