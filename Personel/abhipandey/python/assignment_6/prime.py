def prime1(num):
    if (num == 1):
        return False
    elif (num ==2):
        return True
    else:
        for x in range (2 , num):
            if (num % x==0):
                return False
        return True
num = int(input("enter the num: "))
print("the number is : " , prime1(num)) 