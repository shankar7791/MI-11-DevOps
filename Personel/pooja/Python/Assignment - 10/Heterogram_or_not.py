def hetrogram(input):
    alphabet = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    if len(set(alphabet)) == len(alphabet):
        print("The string is Heterogram")
    else:
        print("The string is not Heterogram")
input = input("\nEnter the string:")
hetrogram(input)