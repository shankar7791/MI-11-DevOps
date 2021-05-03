def sum(num):
    if len(num)==0:
        return 0
    else:
        return num[0] + sum(num[1:]) 
sum= sum([1, 3, 4, 2, 5])
print (sum)





"""def getSum(list,lenth):
    if len==0:
        return 0
    else:
        return list[lenth-1] + getSum(list,lenth-1)
list = (int, input("enter numbers in list ").split())
lenth=len(list)
sum = getSum(list,lenth) 
print (sum)"""
