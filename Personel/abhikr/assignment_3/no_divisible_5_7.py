
# prog 3.1  Program 1 : Write a Python program to find those numbers which a0re divisible by 7 and multiple of 5, between 1500 and 2700


no=[]
for x in range(1500, 2700):
    if (x%7==0) and (x%5==0):
        no.append(str(x))
print (','.join(no))