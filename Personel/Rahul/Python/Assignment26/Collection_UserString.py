from collections import UserString

class MyString(UserString):
    def append(self, s):
        self.data += s

    def remove(self, s):
        self.data = self.data.replace(s, "")

s1 = MyString("PythonProgram")
print("Original String :", s1.data)

s1.append("mming")
print("String After Appending :", s1.data)

s1.remove("Python")
print("String After Removing :", s1.data)