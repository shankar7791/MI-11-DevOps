from collections import UserString

class MyString(UserString):
    def append(self, a):
        self.data += a

    def remove(self, a):
        self.data = self.data.replace(a, "")

s1 = MyString("Avengers Assemble")
print("Original String :", s1.data)

s1.append("\nWakanda forever f")
print("String After Appending :", s1.data)

s1.remove("f")
print("String After Removing :", s1.data)