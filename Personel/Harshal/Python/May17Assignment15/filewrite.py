file = open("/home/harshal/MI-11-DevOps/Personel/Harshal/Python/May17Assignment15/file1.txt", 'w')
lis = [int(item) for item in input("Enter the numbers in the list : ").split()]
print(lis)
file.write(str(lis))
file.close()
