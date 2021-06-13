from collections import UserList

class MyList(UserList):
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")

    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

L = MyList([1, 2 , 3 , 4 , 5 , 6])

print("Original List :")
print(L)
L.append(7)
L.append(8)
print("After Insertion :")
print(L)
L.remove()