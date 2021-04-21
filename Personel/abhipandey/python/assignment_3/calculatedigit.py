s = str(input("enter the word :"))
dig = 0
lett = 0
for i in s :
    if i.isdigit():
        dig +=1
    else :
        lett +=1
print("no of digit is : " , dig)
print("no of letter is :", lett)