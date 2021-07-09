num = int(input("Enter the number :"))
revs_num = 0
while num != 0:
    digit = num % 10
    revs_num = revs_num * 10 + digit
    num = num // 10
print("Reversed Number :" + str(revs_num)) 