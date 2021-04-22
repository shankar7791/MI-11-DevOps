def reve_num(p):
    a = 0
    while True:
        b = str(p)
        if b == b[::-1]:
            break
        else:
            m = int(b[::-1])
            p += m
            a +=1
        return p
print(reve_num(2345))
print(reve_num(3333))