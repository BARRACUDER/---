n=int(input())
first_digit=n%10
counter_lastdigit=0
counter_three=0
counter_chet=0
fifth_sum=0
fact=1
count_zerofive=0
while n>0:
    last_digit=n%10
    if(last_digit==3):
        counter_three+=1
    if(last_digit==first_digit):
        counter_lastdigit+=1
    if last_digit%2==0 and last_digit!=0:
        counter_chet+=1
    if last_digit>5:
        fifth_sum+=last_digit
    if last_digit>7:
        fact*=last_digit
    if last_digit==0 or last_digit==5:
        count_zerofive+=1
    n//=10
print(f"3:{counter_three} \n{first_digit}:{counter_lastdigit} \nчетные:{counter_chet} \nсумма больше 5:{fifth_sum} \nпроизведение чисел больших 7:{fact} \nколичество 0 или 5:{count_zerofive}",sep='')