from collections import UserList

class MyList(UserList):
    def remove(self, s = None):
        raise RuntimeError("Deletion not allowed")

    def pop(self, s = None):
        raise RuntimeError("Deletion not allowed")

L = MyList([1, 2, 3, 4])

print("Original List :")
print(L)
L.append(5)
L.append(6)
print("After Insertion :")
print(L)
L.remove()