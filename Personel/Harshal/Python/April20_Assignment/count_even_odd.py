list = [12, 34, 83, 39, 61, 64, 90, 55, 70, 23, 60, 54, 22]
print("Series of Number is :")
print(list)
even = 0
odd = 0
for i in list :
    if i % 2 == 0 :
        even += 1
    else :
        odd += 1
print(f"Number of even numbers is {even} and odd number is {odd}")