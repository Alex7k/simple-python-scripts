board = [
  "1","2","3",
  "4","5","6",
  "7","8","9"
]
players = ["X", "O"]

def printboard():
  for i in range(3):
    print(f"{board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} ")
    if i < 2: # Don't print line after last row
      print("--|---|--")

def checkwin():
    for player in players:
        for i in range(3):
            # Row
            if board[0+i*3] == board[1+i*3] == board[2+i*3] == player:
               return player
            # Column
            if board[0*3+i] == board[1*3+i] == board[2*3+i] == player:
                return player
            # Diagonal
            if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
               return player
    return False
               

def checkstale():
    for i in board:
       if i not in players:
          return False
    return True

printboard()

while True:
    for player in players:
        while True:
            try:
                chosen_pos = int(input("Wähle ein Feld  ")) - 1
                if board[chosen_pos] not in players:
                    board[chosen_pos] = player
                    break
            except (ValueError, IndexError):
               pass
            print("Invalid position!")
        printboard()

        winstatus = checkwin()
        if winstatus:
           print(f"Player {winstatus} won!")
           exit()
        elif checkstale():
           print("Stalemate!")
           exit()
           
