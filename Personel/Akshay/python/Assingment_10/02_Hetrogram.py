# Check whether a given string is Heterogram or not
def hetro(input):
    alpha = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(alpha)) == len(alpha):
        print("yes")
    else:
        print("no")
input = input("\nenter the string:")
hetro(input)