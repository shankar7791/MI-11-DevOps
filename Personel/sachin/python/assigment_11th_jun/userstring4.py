from collections import UserString

class Mystring(UserString):

    def append(self, s):
        self.data += s

s1 = Mystring("Ram")
print("Original String:", s1.data)
  
s1.append("u")
print("String After Appending:", s1.data)
