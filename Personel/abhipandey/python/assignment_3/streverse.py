def reverse(r):
    if len(r)==0 :
        return r
    else:
        return reverse(r[1:]) + r[0]
r = str(input("enter the word :"))
print("before reversal: " ,r)
print("after reversal: " ,reverse(r))