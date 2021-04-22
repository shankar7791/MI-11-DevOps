def add_without_plus_operator(a,b):
    while b != 0 :
        data = a&b
        a = a^b
        b = data << 1
    return a
print(add_without_plus_operator(10,20))
print(add_without_plus_operator(5,15))
print(add_without_plus_operator(-2,-10))
