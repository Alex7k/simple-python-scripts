import random
import math

### VARIABLES
rows = 50
cols = 50
bombrate = 0.1
bombs = int(rows*cols*bombrate)
# bombs = int(math.sqrt(rows*cols))
################

field = [["_" for x in range(cols)] for y in range(rows)]
bombmap = [["_" for x in range(cols)] for y in range(rows)]

def fillBombs():
  while sum(row.count("*") for row in bombmap) < bombs:
      bombmap[random.randint(0,rows-1)][random.randint(0,cols-1)] = "*"

fillBombs()

def getSpaces(max, text):
  text = str(text)
  spacesAmount = max-len(text)
  spaces = ''
  for i in range(spacesAmount):
    spaces += ' '
  return spaces

def getSurroundingUntouched(row,col):
  surrounding = []
  for colOffset in [-1,0,1]:
    for rowOffset in [-1,0,1]:
      newRow = row+rowOffset
      newCol = col+colOffset
      if field[newRow][newCol] != "_":
        continue
      if colOffset==rowOffset==0 or 0 > newRow or 0 > newCol or newRow >= rows or newCol >= cols: # prevent 0 0 offset and out of bounds bomb checks
        continue
      surrounding.append([newRow,newCol])
  return surrounding

def countSurroundingBombs(row,col):
  count = 0
  for i in getSurroundingUntouched(row,col):
      if bombmap[i[0]][i[1]] == "*":
        count += 1
  if count == 0:
    return " "
  else:
    return str(count)

def flag(row,col):
  if field[row][col] == "_":
    field[row][col] = "F"

def uncover(row,col):
  # Prevent recursion on already uncovered cells
  if field[row][col] != "_":
    return False
  if bombmap[row][col] == "_":
    bombmap[row][col] = "X"
    surroundingBombs = countSurroundingBombs(row,col)
    field[row][col] = surroundingBombs
    if surroundingBombs == " ":
      for i in getSurroundingUntouched(row,col):
        uncover(i[0],i[1])
    # NO BOMB
    return False
  elif bombmap[row][col] == "*":
    # BOMB UNCOVERED
    return True

def printField(show_bombs=False):
  targetField = bombmap if show_bombs else field

  maxDigitsRow = 0
  for row in range(rows):
    length = len(str(row))
    if length > maxDigitsRow:
      maxDigitsRow = length
  maxDigitsCol = 0
  for col in range(cols):
    length = len(str(col))
    if length > maxDigitsCol:
      maxDigitsCol = length

  topLegend = getSpaces(maxDigitsRow+2,"")
  for col in range(cols): # add numbers top legend
    topLegend += str(col+1) + getSpaces(maxDigitsCol+1,col+1)
  print(topLegend)

  for row in range(rows):
    indent = getSpaces(maxDigitsRow+2,row+1)
    # print(indentAmount)
    readableRow = str(row+1)+indent
    for col in range(cols):
      readableRow += targetField[row][col] + getSpaces(maxDigitsCol,"")
    print(readableRow)

printField(False)

while True:
  while True:
    try:
      chosenCol = int(input("Choose a column:"))-1
      chosenRow = int(input("Choose a row:"))-1
      if field[chosenRow][chosenCol] in ["_","F"]:
        break
      else:
        raise
    except:
      print("Choose a different position!")
      continue
  while True:
    action = input("Choose an action -> Hit: 'x', Flag: 'f'").lower()
    if action in ["x","f"]:
      break
    else:
      continue
  if action == "f":
      field[chosenRow][chosenCol] = "F"
      if bombmap[chosenRow][chosenCol] != "*":
        bombmap[chosenRow][chosenCol] = "F"
      printField(False)
      print("Flagged.")
  if action == "x":
    if uncover(chosenRow,chosenCol):
      printField(True)
      print("BOOM. You died!")
      exit()
    else:
      printField(False)
      print("Phew. No bomb.")