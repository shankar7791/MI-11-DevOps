list = [8, 10, 13, 45, 66, 89, 99, 73, 37, 82]
even_number , odd_number = 0 , 0

for num in list :
    if num%2 == 0 :
        even_number += 1
    else :
        odd_number += 1

print("Even_number in the list :", even_number)
print("Odd_number in the list :", odd_number)
