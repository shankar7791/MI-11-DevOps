def prime1(n):
    if (n == 1):
        return False
    elif (n ==2):
        return True
    else:
        for x in range (2 , n):
            if (n % x==0):
                return False
        return True
n = int(input("Enter The Number: "))
print(" Number Is : ",prime1(n)) 