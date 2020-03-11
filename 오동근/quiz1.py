def check369(num):
    check = 0
    while(1):
        if(num % 10 == 3 or num % 10 == 6 or num % 10 == 9) :
            check = 1
            return check
        num = int(num / 10);

        if(num <= 0): break

    return check

for i in range(1,101):
    if(check369(i) == 1): print(str(i) + ' : 짝')

    elif((i % 5) == 0): print(str(i) +' : 아자')

    else: print(i)