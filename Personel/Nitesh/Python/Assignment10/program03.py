def pan(input):
    input = input.lower()
    input = set(input)
    alpha = [ch for ch in input if ord(ch) in range(ord('a'),ord('z')+1)]
    if len(alpha) == 26:
        return "Pangram"
    else:
        return "Not pangram"
input = input("Enter The Sentence : ")
print(pan(input))