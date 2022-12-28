n=int(input()) #ЗАДАЧА С чоколадкой
m=int(input())
k=int(input())
s=n*m
n1=k%n
m1=k%m
if (m1==0 or n1==0) and s>k:
    print("YES")
else:
    print("NO")
