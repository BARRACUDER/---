import numpy as np
a=np.zeros((4,4))
move=list()
for i in range(4):
    n=list(map(str, input().split()))
    move.append(n)

x,y=0,0
for i in range(4):
    for j in range(4):
        if move[i][j]=='r':
            x+=1
        elif move[i][j]=='l':
            x-=1
        elif move[i][j]=='u':
            y+=1
        elif move[i][j]=='d':
            y-=1
    x,y=(x+4)%4,(y+4)%4       
    a[x,y]+=1
    print(a)

a1,a2=np.where(a==2)
print(int(a2),int(a1))

            