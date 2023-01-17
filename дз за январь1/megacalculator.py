x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x=((x1-x2)**2)**0.5
y=((y1-y2)**2)**0.5
if (x==2 and y==1) or (x==1 and y==2):
    print("YES")
else:
    print("NO")
