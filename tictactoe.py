board = [
  "1","2","3",
  "4","5","6",
  "7","8","9"
]
players = ["X", "O"]

def printboard():
  print("--|---|--")
  for i in range(3):
    print(f"{board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} ")
    print("--|---|--")

def checkwin(player):
  for row in range(3):
    if board[0+row*3] == board[1+row*3] == board[2+row*3] == player:
      return True
  for col in range(3):
    if all(board[col+row*3] == player for row in range(3)):
      return True
  if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
    return True
  return False

def checkdraw():
  if all(board[i] in players for i in range(9)):
    return True
  return False


printboard()

player = "X"
while True:
  for player in players:
    input="undefined"
    while True:
      try:
        input = int(input(f"Spieler {player}, wo willst du setzen?: "))
        if input > 9 or input < 1 or (board[input-1] in players):
          print("Invalid position!")
          continue
        else:
          board[input-1] = player
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