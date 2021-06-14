from collections import UserString

class Mystring(UserString):

	def append(self, s):
		self.data += s

	def remove(self, s):
		self.data = self.data.replace(s, "")
	

s1 = Mystring("ram")
print("Original String:", s1.data)


s1.append("u")
print("String After Appending:", s1.data)

s1.remove("r")
print("String after Removing:", s1.data)
