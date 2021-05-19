stri = ["cat", "listen", "tac", "act", "mad", "silent", "dam"]
print("List of String before anagram sort")
print(stri)
anag = {}
for string in stri :
    val = "".join(sorted(string))
    if val in anag.keys() :
        anag[val].append(string)
    else :
        anag[val] = []
        anag[val].append(string)
val = []
for key,value in anag.items() :
    val.append(value)
print("List of String after anagram sort ")
print(val)