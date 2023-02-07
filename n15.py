l=int(input())
m=int(input())
n=list(map(int,input().split()))
k=sorted(n, reverse=True)
ans=0
for i in range(m):
    ans+=n[i]
print(ans)