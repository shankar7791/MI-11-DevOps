for a in range(1,51):
    if a % 3 == 0 and a % 5 == 0:
        print("fizzbuzz")
        continue
    elif a % 3 == 0:
        print("fizz")
        continue
    elif a % 5 == 0:
        print("buzz")
        continue
    print(a)