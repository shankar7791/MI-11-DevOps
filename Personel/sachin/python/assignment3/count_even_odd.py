list = [12,32 , 55, 77 ,776 , 883 , 7654 , 7776 , 44 , 43 , 32 ]
print("Series of Number is :",list)
even = 0
odd = 0
for i in list :
    if i % 2 == 0 :
        even += 1
    else :
        odd += 1
print(f"Number of even numbers is {even} and odd number is {odd}")
