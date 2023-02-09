n=int(input())
ans=0
i=0
while n !=0:
    ans+=(n%3)*(3**i)+(n%3)*3**((i+1))
    n//=3
    i+=2
print(ans)
