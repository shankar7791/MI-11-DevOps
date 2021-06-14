from collections import UserString

class Mystring(UserString):

	def append(self, s):
		self.data += s

	def remove(self, s):
		self.data = self.data.replace(s, "")
	

s1 = Mystring("ram")
print("Original String:", s1.data)

insert_data = input('enter the string to get inerted : ')
s1.append(insert_data)
print("String After Appending:", s1.data)

remove_data = input('enter the string to get removed : ')
s1.remove(remove_data)
print("String after Removing:", s1.data)
