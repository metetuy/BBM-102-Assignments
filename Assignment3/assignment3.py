import sys


def adjacent_cells(row,col,board):
 rows = len(board)
 cols = len(board[0])
 adj_cells=[]
 #check top cell
 if row > 0:
  adj_cells.append(board[row-1][col])
 #check bottom cell
 if row < rows-1:
  adj_cells.append(board[row+1][col])
 #check right cell
 if col > 0:
  adj_cells.append(board[row][col-1])
 #check left cell
 if col < cols-1:
  adj_cells.append(board[row][col+1])
 return adj_cells



#find adjacent cells that have the same value and change them to white space
def change_neighbor(i,j,board,prev_value):
  movement=False
  #check bottom cell
  if i+1 < len(board) and (board[i+1][j]== prev_value):   
      board[i+1][j]=" "
      movement=True
      movement=movement and change_neighbor(i+1,j,board,prev_value)
  #check top cell
  if i > 0 and (board[i-1][j]== prev_value):
      board[i-1][j]=" "
      movement=True
      movement=movement and change_neighbor(i-1,j,board,prev_value)
  #check left cell
  if j > 0 and (board[i][j-1]== prev_value):
      board[i][j-1]=" "
      movement=True
      movement=movement and change_neighbor(i,j-1,board,prev_value)
  #check right cell
  if j+1< len(board[i]) and (board[i][j+1]== prev_value):
      board[i][j+1]=" "
      movement=True
      movement=movement and change_neighbor(i,j+1,board,prev_value)
  adj_cells=adjacent_cells(i,j,board)    
  for x in range(len(adj_cells)):
    if adj_cells[x] == board[i][j]:
     board[i][j]=" "
     movement=True
  return movement

#use a global value for recursions
def prev_val(i,j,board):
 global prev_value
 prev_value=board[i][j]
 return prev_value

#reposition values above if there are
def drop(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if i+1 < len(board) and board[i+1][j]==" ":
        board[i+1][j]=board[i][j]
        board[i][j]=" "
  for i in range(len(board)):
    for j in range(len(board[i])):
        if i+1< len(board) and board[i+1][j]==" " and board[i][j] !=" ":
         drop(board)
  

#evaluate the score
def score_calc():
 global first
 global final
 global prev_value
 count=(first-final)
 score = count*prev_value
 return score
 

#check the board 
def check_board(board):
 for i in range(len(board)):
  for j in range(len(board[i])):
   if board[i][j]!=" ":
    adj_cells=adjacent_cells(i,j,board)
    for x in range(len(adj_cells)):
     if adj_cells[x] == board[i][j]:
      return False
 return True


#check if any of the columns are empty and give the index value
def column_check(board):
  col_list = list(zip(*board))
  for idx, col in enumerate(col_list):
        if all(cell == " " for cell in col):
         return(idx) 
  return None

#move remaining columns left
def column_mover(board,col):
  for i in range(len(board)):
    for j in range(col, len(board[i])-1):
      if j+1 < len(board[i]):
        board[i][j]=board[i][j+1]
    board[i][len(board[i]) - 1] = " "
  return board

#determine the number of numbers that have been changed
def prev_val_count(prev_value,board):
  flat_list = [item for sublist in board for item in sublist]
  global first
  first =flat_list.count(prev_value)
def new_val_count(prev_value,board):
  flat_list = [item for sublist in board for item in sublist]
  global final
  final=flat_list.count(prev_value)


#play the game
def play(board,row,col):
  global score
  global Game_over
  if board[row][col] == " ":
    for r in board:
     print(" ".join(map(str,r)))
    print("\nYou picked an empty space. Please try again.\n")
    return
  prev_val(row,col,board)
  prev_val_count(prev_value,board)
  movement_occured=change_neighbor(row,col,board,prev_value)
  new_val_count(prev_value,board)
  col_to_move = column_check(board)
  if col_to_move is not None:
   column_mover(board,col_to_move)
  score_calc()
  score += score_calc()
  drop(board)
  for r in board:
   print(" ".join(map(str,r)))
  if movement_occured== False:
    print("\nNo movement happened try again\n")
  else: 
   print("\n"+"Your score is:",str(score) + "\n")

  

#open the input file 
input_file_path = sys.argv[1]
with open(input_file_path,"r") as input_file:
 board = [list(map(int,row.strip().split())) for row in input_file]  #make it into a 2d list
 #write output
 for r in board:
   print(" ".join(map(str,r)))
 print()
 print("Your score is: 0\n")
 #take the input cell as row and column
score = 0
Game_over=False
#make the game go on until it is over
while Game_over== False:
 x,y=input("Please enter a row and a column number:").split()
 print()
 row,col=map(int,[x,y])
 if row <= len(board) and col <= len(board[0]): #prevent user from using out of range values
  play(board,row-1,col-1)
  Game_over=check_board(board)
 else:
   print("Please enter a correct size!\n")
   for r in board:
    print(" ".join(map(str,r)))
   print()
else:
  print("Game over!")

   



