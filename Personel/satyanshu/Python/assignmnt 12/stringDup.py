stri = input("Enter a String : ")
stri = stri.lower()
lists = []
for i in range(len(stri)) :
    for j in range(i+1, len(stri)) :
        if stri[i] == stri[j] :
            lists.append(stri[i])
print("Duplicate letters in string are :")
print(set(lists))
