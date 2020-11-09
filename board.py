import os
def display(boardlocal): 
  os.system("printf '\033c'")  
  print (' 1 2 3 4 5 6 7')
  for row in boardlocal:
    print(end=' ')
    for col in row:
        print(col, end=' ')
    print('')
