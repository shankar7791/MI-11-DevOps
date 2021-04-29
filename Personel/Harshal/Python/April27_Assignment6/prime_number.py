def check_prime(num):
    if (num == 1):
        return True
    elif (num ==2):
        return True
    else:
        for x in range (2 , num // 2 ):
            if (num % x==0):
                return False
        return True
num = int(input("Enter a number : "))
if check_prime(num) == True :
    print(f"{num} is Prime")
else :
    print(f"{num} is not Prime")