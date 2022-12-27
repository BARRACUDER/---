a=input()
b=input()
if (a=="желтый" or a=="синий" or a=="красный") and (b=="желтый" or b=="синий" or b=="красный"):
    if a==b:
        ans=a
    elif (a=="желтый" and b=="синий") or (b=="желтый" and a=="синий"):
        ans="зеленый"
    elif (a=="желтый" and b=="красный") or (b=="желтый" and a=="красный"):
        ans="оранжевый"
    else:
        ans="фиолетовый"
else:
    print("ошибка")
print(ans)
