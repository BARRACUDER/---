x=int(input())
y=int(input())
z=int(input())
ans=0
if x==y and x==z:
    ans=3
elif x==y or x==z:
    ans=2
print(ans)
