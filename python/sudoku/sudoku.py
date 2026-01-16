import pygame

pygame.init()

# #### UNFINISHED 2025-06-25

# # - Parameters -

# startDensity = 0.8

# # --

# length = 9
# board = [["-" for x in range(length)] for y in range(length)]

# # def fillBombs():
# #   while sum(row.count("*") for row in board) < bombs:
# #       board[random.randint(0,rows-1)][random.randint(0,cols-1)] = "*"

# def valid_num(number):
#   if number in range(9):
#     return True
#   return False

# def valid_chars():
#   for row in range(length):
#     for col in range(length):
#       if board[row][col] not in list(range(9)) + ["-"]:
#         return False
#   return True

# def valid():
#   if not valid_chars():
#     return False
#   for row in board:
#     row_temp = row.copy()
#     for col in row:
#       del row_temp[index(col)]
#       if col in


# print("Valid: " + str(valid()))


# def print_board():
#   for row in range(length):
#     printable_line = ""
#     if (row) % 3 == 0 and 0 < row < length-1:
#       print("---------------------")
#     for col in range(length):
#       if (col + 1) % 3 == 0 and col < length-1:
#         divider = " | "
#       else:
#         divider = " "
#       printable_line += board[row][col] + divider
#     print(printable_line)

# print_board()
