import board
import time
import win
import sys
import play
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 
def delete_last_lines(num):
  for i in range(num):
    sys.stdout.write(CURSOR_UP_ONE) 
    sys.stdout.write(ERASE_LINE) 
#it is in a function so I can come out of multiple loops at once
          
#this keeps it in a loop so it can restart/clear while the code is running
while True: 
  board1 = [
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
  ]
  board.display(board1)
  playing = True   
  while playing:     
    #this is the player moves
    play.move(board1, 'X',playing)
    # this ends the game when someone wins
    if win.check(board1,'X'): break
    play.move(board1, '0',playing)
    # this ends the game when someone wins
    if win.check(board1,'0'): break
    y = 0
    full_all = 0
    #this checks if the board it full and if it is it restarts
    for i in board1:
        #this is needed so it doesnt stop when it encounters a full row
        if not ' ' in board1[y]:
            full_all+=1
        #this is needed so it doesnt stop when it encounters a full row
        if full_all == 6:
          playing = False
          print('  The board is full')
          time.sleep(5)
          break
        y += 1
