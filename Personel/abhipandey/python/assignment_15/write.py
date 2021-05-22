file = open("/home/abhishek/MI-11-DevOps/Personel/abhipandey/python/assignment_15/file1.txt", 'w')
lis = [int(item) for item in input("Enter the numbers in the list : ").split()]
print(lis)
file.write(str(lis))
file.close()