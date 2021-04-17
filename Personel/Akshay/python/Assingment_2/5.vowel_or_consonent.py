#check vowel
l = input("Enter the character: ")
if l.lower() in ('a', 'e', 'i', 'o', 'u'):
  print("Vowel")
elif l.upper() in ('A', 'E', 'I', 'O', 'U'):
  print("Vowel")
else:
  print("Consonant")