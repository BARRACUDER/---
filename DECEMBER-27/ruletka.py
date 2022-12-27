x=int(input())
red="красный"
blk="чёрный"
n=x%2
if x==0:
    ans="зеленый"
elif 1<=x<=10:
    if n==0:
        ans=blk
    else:
        ans=red
elif 11<=x<=18:
    if n==0:
        ans=red
    else:
        ans=blk
elif 19<=x<=28:
    if n==0:
        ans=blk
    else:
        ans=red
elif 29<=x<=36:
    if n==0:
        ans=red
    else:
        ans=blk
else:
    ans="ошибка"
print(ans)
