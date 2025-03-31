import sys 

#layout restrictions
def hbn(board):
    return board[0],board[1],board[2],board[3]

#take cols as rows checking them will be easier
def transpose(board):
  cols = list(zip(*board))
  return cols


#check if the game is over or not
def check_board(b1):
  count=0
  for row in b1:
        if row.count("R") > 0 or row.count("D") > 0:
            count +=1 # There are still "R" or "D" characters on the board
  if count > 0:
    return True
  return False  # No more "R" or "D" characters on the board

#board setter
def temp(board): 
    return board[4:]


    
#is the change valid
def is_val(r,c,board,b1):
    row_highs,row_bases,col_highs,col_bases= hbn(board)
    #create a appropriate cols list
    cols = transpose(b1)
    #check if the changes are valid or not
     #for col and row restrictions
    for i,j in enumerate(row_highs):
     if j != -1:
        if (b1[i].count("U")== 0 and b1[i].count("L")==0 and b1[i].count("R")==0 and b1[i].count("D")== 0 and b1[i].count("H") != j):
         return False
    for i,j in enumerate(row_bases):
     if j != -1:
        if (b1[i].count("U")== 0 and b1[i].count("L")==0 and b1[i].count("R")==0 and b1[i].count("D")== 0 and b1[i].count("B") != j):
         return False
    for i,j in enumerate(col_highs):
     if j != -1:
      if (cols[i].count("U")== 0 and cols[i].count("L")==0 and cols[i].count("R")==0 and cols[i].count("D")== 0 and cols[i].count("H") != j):
        return False
    for i,j in enumerate(col_bases):
     if j !=-1:
      if (cols[i].count("U")== 0 and cols[i].count("L")==0 and cols[i].count("R")==0 and cols[i].count("D")== 0 and cols[i].count("B") != j):
       return False
    #check the adjacent cells of every cell
    for r in range(len(b1)):
      for c in range(len(b1[0])):
        #check inside cells
        if r+2<=len(b1) and c+2<= len(b1[0]): 
         if b1[r][c]== "H" and (b1[r][c+1]=="H" or (c!=0 and b1[r][c-1]=="H") or b1[r+1][c]== "H" or (r!=0 and b1[r-1][c]=="H")):
             return False
         if b1[r][c]== "B" and ((c!=0 and b1[r][c-1]=="B") or (r!=0 and b1[r-1][c]=="B") or b1[r+1][c]== "B" or b1[r][c+1] == "B"):
           return False
        #check edge cells 
        elif r <= len(b1) and c <= len(b1[0]):
           if b1[r][c] == "H" and ((c!=0 and b1[r][c-1]=="H") or (r!=0 and b1[r-1][c]=="H")):
              return False
           if b1[r][c] == "B" and ((c!=0 and b1[r][c-1]=="B") or (r!=0 and b1[r-1][c]=="B")):
             return False
    return True

def val_cH(r,c,b1,b,prev_tile,template,f):
 #since len(b1) = r +1 for the last row if the row hits the edge return True
 if r == len(b1):
   return True
 if b1[r][c]== "L":
  b1[r][c],b1[r][c+1]="H","B"

  #if the board is not valid change the tile to its original state and return false
  if is_val(r,c,b,b1)==False:
     b1[r][c],b1[r][c+1]="L","R"
     return False
  

  if c+2 < len(b1[0]):
    #start the process again for position(r,c+2)
    val_change_gen(r, c + 2, b1, b, (r, c),template,f)
  elif r+1<= len(b1):
    #make c=0 so it moves to the begining of the next row and start the process again for position (r+1,0)
    val_change_gen(r + 1, 0, b1, b, (r,c),template,f)
 
 
 #change in vertical way
 if b1[r][c]=="U":
  b1[r][c],b1[r+1][c]="H","B"
  #if the board is not valid after the move change the (r,c)(r+1,c) position to its original state
  if is_val(r,c,b,b1)==False:
    b1[r][c],b1[r+1][c]="U","D"
    return False
 
 
  if c+1 < len(b1[0]):
   val_change_gen(r,c+1,b1,b,(r,c),template,f)
  elif r+1<= len(b1):
    val_change_gen(r+1,0,b1,b,(r,c),template,f)

 
 elif (template[r][c]=="D" or template[r][c]=="U")and (b1[r][c]=="H"or b1[r][c]=="B" or b1[r][c]=="N") :
  if c+1<len(b1[0]):
   val_cH(r,c+1,b1,b,prev_tile,template,f)
  elif r+1<len(b1):
    val_cH(r+1,0,b1,b,prev_tile,template,f)
           
           
def val_cB(r,c,b1,b,prev_tile,template,f):
 #since len(b1) = r +1 for the last row if the row hits the edge return True
 if r == len(b1):
   return True
 if b1[r][c]=="L":
  b1[r][c],b1[r][c+1]="B","H"

  #if the board is not valid change the tile to its original state and return false
  if is_val(r,c,b,b1)==False:
     b1[r][c],b1[r][c+1]="L","R"
     return False
  
  
  if c+2 < len(b1[0]):
    #start the process again for position(r,c+2)
    val_change_gen(r, c + 2, b1, b, (r, c),template,f)
  elif r+1<= len(b1):
    #make c=0 so it moves to the begining of the next row and start the process again for position (r+1,0)
    val_change_gen(r + 1, 0, b1, b, (r,c),template,f)


 if b1[r][c]=="U":
  b1[r][c],b1[r+1][c]="B","H"
  #if the board is not valid change the tile to its original state and return false
  if is_val(r,c,b,b1)==False:
    b1[r][c],b1[r+1][c]="U","D"
    return False

  
  if c+1< len(b1[0]):
   #starts the process again for next cell (r,c+1)
   val_change_gen(r,c+1,b1,b,(r,c),template,f)
  elif r+1<= len(b1):
    #make c=0 so it moves to the begining of the next row and start the process again for position (r+1,0)
    val_change_gen(r+1,0,b1,b,(r,c),template,f)
  
  
  
  #if next tile is full move one cell right or to the beginning of the next row
 elif (template[r][c]=="D" or template[r][c]=="U")and (b1[r][c]=="H"or b1[r][c]=="B" or b1[r][c]=="N") :
  if c+1<len(b1[0]):
   val_cB(r,c+1,b1,b,prev_tile,template,f)
  elif r+1<len(b1):
    val_cB(r+1,0,b1,b,prev_tile,template,f)




def val_cN(r,c,b1,b,prev_tile,template,f):
    #since len(b1) = r +1 for the last row if the row hits the edge return True
    if r == len(b1):
     return True
    #if tile starts with L consider change on a horizontal way
    if b1[r][c]=="L":
     #change the tile to NN
     b1[r][c],b1[r][c+1]="N","N"
     #if the board is not valid change the tile to its original state and return false
     if is_val(r,c,b,b1)==False:
      b1[r][c],b1[r][c+1]="L","R"
      return False
    
     if c+2 < len(b1[0]):
      val_change_gen(r, c + 2, b1, b, (r, c),template,f)
     elif r+1<= len(b1):     
      #make c=0 so it moves to the begining of the next row and start the process again for position (r+1,0)
      val_change_gen(r + 1, 0, b1, b, (r,c),template,f) 
   
   
   
   
    #if the tile start with U:
    if  b1[r][c]=="U":
      #change the tile to NN
      b1[r][c],b1[r+1][c]="N","N"
      #if the board is not valid after the move change the (r,c)(r+1,c) position to its original state
      if is_val(r,c,b,b1)==False:
       b1[r][c],b1[r+1][c]="U","D"
       return False
      

      #if the c+1 does not extend the limits of the board:
      if c+1 < len(b1[0]):
       val_change_gen(r,c+1,b1,b,(r,c),template,f)
      elif r+1<= len(b1):
        val_change_gen(r+1,0,b1,b,(r,c),template,f)



    #if next tile is full move one cell right or to the beginning of the next row      
    elif (template[r][c]=="D" or template[r][c]=="U")and (b1[r][c]=="H"or b1[r][c]=="B" or b1[r][c]=="N") :
        if c+1<len(b1[0]):
          val_cN(r,c+1,b1,b,prev_tile,template,f)
        elif r+1<len(b1):
           val_cN(r+1,0,b1,b,prev_tile,template,f)






#recursion function for master branch
def val_change_gen(r,c,b1,b,prev_tile,template,f):


 #first branch HB
     if val_cH(r,c,b1,b,prev_tile,template,f):
       return True
     
     else:
       if not check_board(b1):
         return True
       #new previous tile will stay the same
       new_prev_tile=prev_tile

     
     
     
  #second branch BH
     if val_cB(r,c,b1,b,new_prev_tile,template,f):
        return True
     
     
     
     else:
       if not check_board(b1):
         return True
       #new previous tile will stay the same
       new_prev_tile=prev_tile

      
     
     
  #third branch NN
     if val_cN(r,c,b1,b,new_prev_tile,template,f):
       return True
     
     else:
      if not check_board(b1):
         return True
     try:
      #r,c will be the last worked tile and will be returned to its original state
      r, c = new_prev_tile

      if template[r][c] == "U":
            b1[r][c], b1[r+1][c] = "U", "D"
      
      if template[r][c] == "L":
            b1[r][c], b1[r][c+1] = "L", "R"
      new_prev_tile=prev_tile
     except TypeError:
       f.write("No solution!")
       f.close()
   
   

def solve(b,template,f):
    b1=temp(b)
    r=0
    c=0
    #start
    val_change_gen(r,c,b1,b,None,template,f)
    return b1

             



def main():
   
    input_file_path=sys.argv[1]
    output_file_path=sys.argv[2]
    with open(input_file_path,"r") as input_file, open(output_file_path,"w") as output_file:
        board1 =[list(map(str,line.split())) for line in input_file] #Turn the given input to a 2d list]
        int_board=[list(map(int,line)) for line in board1[:4]]#take first 4 lines as integers
        str_board=[list(map(str,line)) for line in board1[4:]]#take other lines as strings
        board=int_board+str_board
        b1=temp(board)
        template= [row[:] for row in b1]#create a template to preserve the original template
        new_board=solve(board,template,output_file)
        try:
         for line in new_board:
          output_file.write(" ".join(map(str,line))+"\n")
        except ValueError:
          pass
      
      

        

if __name__ == "__main__":
    main()