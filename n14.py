from random import randint
n=int(input())
win=0
while win == 0:
    a=randint(-999999999999,9999999999999)
    print(f"{a}, это ваше число")
    ans=input("Да или Нет \n")
    if ans=="да":
        if a==n:
            win=1
        else:
            print("Вы соврали")
    else:
        if a==n:
            print("вы соврали")
    
print("я так и знала")
