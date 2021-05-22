file = open("/home/abhishek/MI-11-DevOps/Personel/abhipandey/python/assignment_15/file1.txt", 'r')
val = file.read()
val = val.strip("[")
val = val.strip("]")
val = val.split(", ")
lis = []
for line in val:
    lis.extend(map(int, line.split(',')))

print(sorted(lis))
file.close()