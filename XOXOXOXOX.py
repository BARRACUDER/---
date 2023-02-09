import numpy as np
def out_field(field,field_size):
    for i in range(field_size):
        
        for j in range(field_size):
            if field[i,j]==0:
                print("| _ ",end='')
            elif field[i,j]==1:
                print("| X ",end='')
            else:
                print("| O ",end='')
        print('|',end='\n')
    print('\n')

win=0
turn=1
field_size=int(input())
win_size=int(input())
field=np.zeros((field_size,field_size))
while win==0 and 0 in field:
    out_field(field,field_size)
    right=0
    while right==0:
        x,y=map(int,input().split())
        if  x>=field_size or y>=field_size or x<0 or y<0 or field[x,y]!=0:
            print("mistake,try again")
        else:
            right=1
    if turn%2==0:
        field[x,y]=1 #X
    else:
        field[x, y] = 2 #O
    turn+=1
    count_x=0
    count_O=0




    for i in range(field_size):
        for j in range(field_size):

            for k in field[i:i+win_size+1,j]:
                if k==1:
                    count_x+=1
                elif k==2:
                    count_O+=1

            if count_O == win_size or count_x==win_size:
                win=1
                break
            else:
                count_x = 0
                count_O = 0


            for k in field[i,j:j+win_size+1]:
                if k==1:
                    count_x+=1
                elif k==2:
                    count_O+=1

            if count_O == win_size or count_x==win_size:
                win=1
                break
            else:
                count_x = 0
                count_O = 0

            for k in range(win_size):
                try:
                    if field[i+k,j+k]==1:
                        count_x += 1
                    elif field[i+k,j+k] == 2:
                        count_O+=1
                except IndexError:
                    pass

            if count_O == win_size or count_x == win_size:
                win = 1
                break
            else:
                count_x = 0
                count_O = 0

            for k in range(win_size):
                try:
                    if field[i + k, j - k] == 1:
                        count_x += 1
                    elif field[i + k, j - k] == 2:
                        count_O += 1
                except IndexError:
                    pass

            if count_O == win_size or count_x==win_size:
                win=1
                break
            else:
                count_x = 0
                count_O = 0
out_field(field,field_size)
if win==0:
    print("Ничья")
if count_O==win_size:
    print("O-WINS")
else:
    print("X-wins")

