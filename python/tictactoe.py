board = [
  "1","2","3",
  "4","5","6",
  "7","8","9"
]
players = ["X", "O"]

def printboard():
  for i in range(3):
    print(f"{board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} ")
    if i < 2: # avoid printing line after last row
      print("--|---|--")

def checkwin(player):
  for row in range(3):
    if all(board[row*3 + col] == player for col in range(3)):
      return True
  for col in range(3):
    if all(board[row*3 + col] == player for row in range(3)):
      return True
  if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
    return True
  return False

def checkdraw():
  return all(board[i] in players for i in range(9))

printboard()

while True:
  for player in players:
    playerinput = "undefined"
    while True:
      try:
        playerinput = int(input(f"Player {player}, select a position (1-9): "))
        if not (1 <= playerinput <= 9) or board[playerinput-1] in players:
          print("Invalid position!")
          continue
        else:
          board[playerinput-1] = player
          break
      except ValueError:
        print("Please enter a valid number!")
        continue

    printboard()

    if checkwin(player):
      print(f"{player} wins!")
      exit()
    if checkdraw():
      print("Draw!")
      exit()