x=int(input())
y=int(input())
z=int(input())
ans=0
if x==y or z==y:
    ans=2
if x==y and x==z:
    ans=3
print(ans)
