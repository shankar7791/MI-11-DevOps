def sum(a):
    if a <= 1:
        return a
    else:
        return a + sum(a-1)

num = int(input("Enter a number: "))
print("The sum is: ", sum(num))