#The idea: Wanna try my hand at minimax with tic-tac-toe
#Make 3-by-3 arrays to store the game state. X (+1) goes first, O (-1) goes next. Keep a running list of available moves to easily draw from


from numpy import zeros, prod, copy, array
from random import randint

def Minimax(board, moves):
  bestmove=[-1,-1]
  score=-2

  #X's turn
  if len(moves)%2==1:
    n=0
    score=-2
    #Keep trying moves until you find a winning one, or all moves are exhausted
    while score!=1 and n<len(moves):
      board2=copy(board)
      board2[moves[n][0],moves[n][1]]=1
      termcheck=Terminal(board2)

      #If the board isn't done, have your opponent try their moves      
      if termcheck==-2:
        moves2=moves.copy()
        moves2.remove(moves[n])
        result=Minimax(board2,moves2)[1]
        if result>score:
          score=result 
          bestmove=moves[n]
      
      #If the board IS done, score it and see if it's a better move than you already had.
      elif termcheck>score:
        score=termcheck
        bestmove=moves[n]

      n+=1
      
  #O's turn
  if len(moves)%2==0:
    n=0
    score=2
    #Keep trying moves until you find a winning one, or all moves are exhausted
    while score!=-1 and n<len(moves):
      board2=copy(board)
      board2[moves[n][0],moves[n][1]]=-1
      termcheck=Terminal(board2)

      #If the board isn't done, have your opponent try their moves      
      if termcheck==-2:
        moves2=moves.copy()
        moves2.remove(moves[n])
        result=Minimax(board2,moves2)[1]
        if result<score:
          score=result 
          bestmove=moves[n]
      
      #If the board IS done, score it and see if it's a better move than you already had.
      elif termcheck<score:
        score=termcheck
        bestmove=moves[n]

      n+=1    

  return bestmove, score

#Display the board as Xs and Os, for aesthetics
def Display(board):
  disboard=zeros([3,3],str)

  for m in range(3):
    for n in range(3):
      disboard[m,n]=' '
      if board[m,n]==1:
        disboard[m,n]='X'
      if board[m,n]==-1:
        disboard[m,n]='O'

  print(disboard)

#See if the board has reached an end state, either someone won or the board is filled.
def Terminal(board):
  winner=-2

  #Check the rows
  for m in range(3):
    if sum(board[m,:])==3 or sum(board[m,:])==-3:
      #print(f'3 in a row at row {m}!')
      winner=sum(board[m,:])/3

  #Check the cols
  for n in range(3):
    if sum(board[:,n])==3 or sum(board[:,n])==-3:
      #print(f'3 in a row at col {n}!')
      winner=sum(board[:,n])/3

  #Check the diags
  if board[0,0]+board[1,1]+board[2,2]==3 or board[0,0]+board[1,1]+board[2,2]==-3:
    #print(f'3 in a row on the negative diagonal!')
    winner=(board[0,0]+board[1,1]+board[2,2])/3

  if board[0,2]+board[1,1]+board[2,0]==3 or board[0,2]+board[1,1]+board[2,0]==-3:
    #print(f'3 in a row on the positive diagonal!')
    winner=(board[0,2]+board[1,1]+board[2,0])/3 

  #Check if the board is full, and whether someone has won per the above.
  if prod(board)!=0 and winner==-2:
    winner=0
  
  return winner

#board=zeros([3,3],int)
board=array([[0,-1,0],[0,1,0],[1,0,0]],int)

#Keep track of what squares are available, rather than check for 0s every time by looping over the board.
moves=[]
for m in range(3):
  for n in range(3):
    if board[m,n]==0:
      moves.append([m,n])

#Have the players take turns
#turn=0
#while Terminal(board)==-2:
#  #Display(board)
#  #print('')

#  #X's turn
#  if turn%2==0:
#    square=moves[randint(0,len(moves)-1)]
#    board[square[0],square[1]]=1
#    moves.remove(square)

#  #O's turn
#  else:
#    square=moves[randint(0,len(moves)-1)]
#    board[square[0],square[1]]=-1
#    moves.remove(square)

#  turn+=1

#board[0,1]=1
#moves.remove([0,1])

while Terminal(board)==-2:
  Display(board)
  move,score=Minimax(board,moves)
  print(move)
  print(score)
  moves.remove(move)
  if len(moves)%2==0:
    board[move[0],move[1]]=1
  else:
    board[move[0],move[1]]=-1

Display(board)

if Terminal(board)!=-2:
  if Terminal(board)==1:
    print('X wins!')
  if Terminal(board)==-1:
    print('O wins!')
  if Terminal(board)==0:
    print('It is a tie!')

#Notes:
#It works! But not ideally. The main thing that goes wrong is that if a player has no moves that prevent a win, they don't differentiate between them.
#For instance, suppose we have this board:
# _O_
# _X_
# X__
#Nothing O does can stop X from winning. If they try, you get the sequence
# _OO
# _X_
# X__
#--------
# XOO
# _X_
# X__
#--------
# XOO
# _X_
# X_O
#--------
# XOO
# XX_
# X_O
#--------
#But because O knows it can't win, instead of playing 'intelligently', it does this:
# OO_
# _X_
# X__
#--------
# OOX
# _X_
# X__
#--------
#It does this because, as far as O is concerned, both moves are the same; they both end in a loss. But by delaying the loss, you open your opponent
#up to making a mistake. Need to add a way to incorporate this. That, or accept that this code can find winning moves, but doesn't avoid obviously losing
#ones. Maybe keep a running track of how deep the code is looking, and prefer moves with greater depth (unless they're winning). 
