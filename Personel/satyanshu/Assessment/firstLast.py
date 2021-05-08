
def firstLast(numberList):
    print("list is ", numberList)
    firstElement = numberList[0]
    lastElement = numberList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False

numList = [10, 20, 30, 40, 50]
print("result is", firstLast(numList))
