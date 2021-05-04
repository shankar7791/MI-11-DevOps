def pan(input):
    input = input.lower()
    input = set(input)
    alpha = [ch for ch in input if ord(ch) in range(ord('a'),ord('z')+1)]
    if len(alpha) == 26:
        return "pangram"
    else:
        return "not pangram"
input = input("\n enter the sentence : ")
print(pan(input))