list = []

num = int(input("Enter number of elments in list: "))
for i in range(1, num + 1):
    elments = int(input("Enter number: "))
    list.append(elments)

print("Largest number is :", max(list))

