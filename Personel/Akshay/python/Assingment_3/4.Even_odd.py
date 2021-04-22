list = [10,11,22,44,13,66,23,90,5,4,26,24]
print("Series of Number is :")
print(list)
even = 0
odd = 0
for i in list :
    if i % 2 == 0 :
        even += 1
        print("Number is even")
    else :
        odd += 1
        print("Number is odd")
