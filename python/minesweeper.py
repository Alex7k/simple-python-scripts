import random
import math

### VARIABLES
rows = 13
cols = 13
bombDensity = 0.1
bombs = int(rows*cols*bombDensity)
# bombs = int(math.sqrt(rows*cols))
################

field = [["-" for x in range(cols)] for y in range(rows)]
bombmap = [["-" for x in range(cols)] for y in range(rows)]

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

def getSurrounding(row,col):
  surrounding = []
  for colOffset in [-1,0,1]:
    for rowOffset in [-1,0,1]:
      newRow = row+rowOffset
      newCol = col+colOffset
      if colOffset==rowOffset==0 or 0 > newRow or 0 > newCol or newRow >= rows or newCol >= cols: # prevent 0 0 offset and out of bounds bomb checks
        continue
      surrounding.append([newRow,newCol])
  return surrounding

def countSurroundingBombs(row,col):
  count = 0
  for i in getSurrounding(row,col):
    if bombmap[i[0]][i[1]] == "*":
      count += 1
  if count == 0:
    return " "
  else:
    return str(count)

def flag(row,col):
  if field[row][col] == "-":
    field[row][col] = "F"

def uncover(row,col):
    # Iterative flood fill to avoid recursion limit
    stack = [(row,col)]
    while stack:
        r, c = stack.pop()
        if field[r][c] != "-":
            continue
        if bombmap[r][c] == "*":
            return True  # BOMB UNCOVERED
        surroundingBombs = countSurroundingBombs(r, c)
        field[r][c] = surroundingBombs
        if surroundingBombs == " ":
            for nr, nc in getSurrounding(r, c):
                if field[nr][nc] == "-":
                    stack.append((nr, nc))
    return False

def printField(showBombs=False):
  if showBombs:
    # Deep copy of field
    fieldDisplay = [row[:] for row in field]
    for row in range(rows):
      for col in range(cols):
        if bombmap[row][col] == "*":
          fieldDisplay[row][col] = "*"
  else:
    fieldDisplay = field

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
      readableRow += fieldDisplay[row][col] + getSpaces(maxDigitsCol,"")
    print(readableRow)

printField(False)

while True:
  while True:
    try:
      chosenCol = int(input("Choose a column:"))-1
      chosenRow = int(input("Choose a row:"))-1
      if field[chosenRow][chosenCol] in ["-","F"]:
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