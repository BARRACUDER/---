x=int(input())
y=int(input())
z=int(input())
ans=0
if x==y or z==y or z==x:
    ans=2
if x==y and x==z and z==y:
    ans=3
print(ans)