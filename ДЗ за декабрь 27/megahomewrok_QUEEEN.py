x1=int(input()) #ЗАДАЧА С ферзееем
y1=int(input())
x2=int(input())
y2=int(input())
n1=x2-x1
n2=y2-y1
if n1<0:
    n1=-n1
if n2<0:
    n2=-n2
if n1==n2 or x1==x2 or y1==y2:
    print("YES")
else:
    print("NO")