import sys

#Find empty cells
def find_empty(sudoku):
 for row in range(len(sudoku)):
    for col in range(len(sudoku)):
        if sudoku[row][col]==0:
           return row,col
 return(None,None)

#Check whether the guess is appropriate for row, column and 3x3 subgrid
def is_valid(sudoku,guess,row,col):
  row_st= (row//3) *3
  col_st= (col//3) *3 
  for r in range(row_st,row_st+3):
   for c in range(col_st,col_st+3):
     if sudoku[r][c]==guess:
       return False

  
  col_value=[sudoku[i][col] for i in range(9)]

  
  if guess in sudoku[row]:
    return False
  if guess in col_value:
    return False
  return  True

#Find the cells with only one possible value
def find_single_value_cells(sudoku):
    single_value_cells = []

    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                possible_values = []
                for guess in range(1, 10):
                    if is_valid(sudoku, guess, row, col):
                        possible_values.append(guess)

                if len(possible_values) == 1:
                    single_value_cells.append((row, col, possible_values[0]))

    return single_value_cells



#Write the expected output to the output file
def print_steps(sudoku, i, guess, row, col, output_file):
       output_file.write("-"*18+"\n")
       output_file.write("Step {} - {} @ R{}C{}\n".format(i,guess,row+1,col+1))
       output_file.write("-"*18+"\n")
       for r in sudoku:
          output_file.write(" ".join(map(str,r))+"\n")



def solve(sudoku,output_file,i=1):
   row,col = find_empty(sudoku)
   if row is None:      #If none of the row is empty stop the function
     return True
   single_value_cells = find_single_value_cells(sudoku)     
   while single_value_cells:        #Loop through single value cells 
      row, col, guess = single_value_cells[0]   #Change the value of the first single value cell
      sudoku[row][col] = guess
      print_steps(sudoku,i,guess,row,col,output_file)
      i+=1
      single_value_cells = find_single_value_cells(sudoku) #Check the sudoku board again after the placement of values in order to find new single value cells





def main():
    input_file_path= sys.argv[1] 
    output_file_path= sys.argv[2]
    with open (input_file_path,"r") as input_file, open (output_file_path,"w") as output_file: 
     sudoku = [list(map(int,line.strip().split())) for line in input_file] #Turn the given input to a 2d list
     solve(sudoku,output_file)
     output_file.write("-"*18)
    




if __name__=="__main__":
    main()