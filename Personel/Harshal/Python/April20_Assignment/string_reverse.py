str_val = input("Enter a String : ")
str_list=[]
for i in str_val :
    str_list.append(i)
str_list.reverse()
rev_str = "".join([str(i) for i in str_list])
print(rev_str) 