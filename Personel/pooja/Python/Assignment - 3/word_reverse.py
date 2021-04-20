word = input("Enter the word :")
for char in range(len(word) -1, -1, -1):
    print(word[char],end="")
print("\n")