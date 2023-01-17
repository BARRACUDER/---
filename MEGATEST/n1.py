a=int(input())
a1=a%10
a2=(a//10)%10
if a<100:
    print("NO")
elif a1==a2==0:
    print("YES")
else:
    print("NO")