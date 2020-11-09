import time
import win
import board
def move(boardlocal,piece,playing):
      #not_full is for the collumns
      not_full = True
      #not_full tells whether the collum is full without losing there go
      #player one move
      while not_full:
          play = [1, 2]
          #this tries to place the piece and if it cant it the input is not a number(or restart)
          try:
            #this checks whether the number is in the range of the boardlocal
            while not len(play) == 1 or not int(play[0]) < 8:
                play = list(input('  Choose a collum.  '))
                not_valid = False
                if (not len(play) == 1 or not int(play[0]) < 8 ):
                    print('  That is not a valid space.')
                    not_valid = True
                    time.sleep(0.5)
                    board.display(boardlocal)
                #if you tell it to restart it comes out of the function and since the function is put in a while loop it restarts and clears the boardlocal
          except:
            print('  That is not a number')
            time.sleep(1)
          bottom = 5
          #this tries to place the piece at the lowest point it can and if it cant place it the collum is full.
          try:
            #this checks whether the number is in the range of the boardlocal
              while boardlocal[bottom][(int(play[0]) - 1)] == '0' or boardlocal[bottom][(int(play[0]) - 1)] == 'X':
                  bottom -= 1
              if not boardlocal[bottom][(int(play[0]) - 1)] == '0' or not boardlocal[bottom][(int(play[0]) - 1)] == 'X':
                  boardlocal[bottom][(int(play[0]) - 1)] = piece
              not_full = False
          except:
              #tells the players the collum is full
              print('  That collum is full.')
              time.sleep(0.5)
              not_full = True
          board.display(boardlocal)
          #checks if that move wins
          if not not_valid:
            if win.check(boardlocal,piece) == True:
              print('  ',piece,'\'s win the game!')
              time.sleep(2)
              playing = False
              return playing
      not_full = True
