num = int(input("Multiplication using value? : "))

while num <= 10:
    i = 1
    while i <= num:
        product = num*i
        print(num, " * ", i, " = ", product, "\n")
        i = i + 1
    print("\n")
    num = num + 1