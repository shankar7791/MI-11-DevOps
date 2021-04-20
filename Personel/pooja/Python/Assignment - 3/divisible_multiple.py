num = []
for x in range (10,200):
    if( x%7==0) and (x%5==0):
        num.append(str(x))
print(','.join(num))