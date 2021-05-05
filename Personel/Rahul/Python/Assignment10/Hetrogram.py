def hetro(input):
    alpha = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(alpha)) == len(alpha):
        print("yes")
    else:
        print("no")
input = input("Enter The String:")
hetro(input)