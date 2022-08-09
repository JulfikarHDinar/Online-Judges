inp = list(map(int,input().split())) 
N = inp[0]
M = inp[1]
#N * M               7 * 21
midrow = 0
for i in range(N):
  #first rows
  if i < int(N/2):  
    lasthyph=0
    lastcann=0
    for j in range(int( ((M-3)/2)-i*3 )):
      print('-',end='')#first hyphens
      lasthyph=lasthyph+1
    
    for j in range(int( i*2+1 )):
      print('.|.',end='')#middle cannons
      lastcann=lastcann+1

    for j in range(int( ((M-3)/2)-i*3 )):
      print('-',end='')#last hyphens

  #middle row
  if i == int(N/2):  
    midrow = i
    for j in range(int( (M-7)/2 )):
      print('-',end='')#first hyphens
    
    print('WELCOME',end='')
    
    for j in range(int( (M-7)/2 )):
      print('-',end='')#last hyphens

  #last rows
  if i > int(N/2):  
    for j in range(lasthyph * (i-midrow)):
      print('-',end='')#first hyphens
      
    for j in range(lastcann - 2 *(i-midrow-1) ):
      print('.|.',end='')#middle cannons

    for j in range(lasthyph * (i-midrow)):
      print('-',end='')#last hyphens
  print("")#line end
