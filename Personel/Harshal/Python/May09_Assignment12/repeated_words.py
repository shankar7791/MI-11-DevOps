stri = input("Enter a sentence : ")
stri = stri.lower()
split = stri.split()
val = []
for i in split :
    if i not in val :
        val.append(i)
print(val)