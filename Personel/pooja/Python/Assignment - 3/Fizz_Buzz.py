for FizzBuzz in range(1,49):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print ("FizzBuzz")
        continue
    elif FizzBuzz % 3 == 0:
        print("Fizz")
        continue
    elif FizzBuzz % 5 == 0:
        print("Buzz")
        continue
    print(FizzBuzz)