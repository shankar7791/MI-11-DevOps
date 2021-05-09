from itertools import groupby

def group_by(stri) :
    val = [] 
    for (key,group) in groupby(stri) :
        val.append(key)
    
    str1 = ''.join(val)
    print(str1)

stri = input("Enter a String : ")
group_by(stri)