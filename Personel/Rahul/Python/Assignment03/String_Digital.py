s = input("Enter The String")
d=0
l=0
for c in s:
    if c.isdigit():
        d=+1
    elif c.isalpha():
        l=+1
    else:
        pass
print("Number of Letter is:", l)
print("Number of Digits String:", d)
