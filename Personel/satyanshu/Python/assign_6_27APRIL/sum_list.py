list = map(int, input("enter numbers in list ").split())
def sum(numbers):
    total = 0
    for x in list:
        total += x
    return total
print(sum(list))
