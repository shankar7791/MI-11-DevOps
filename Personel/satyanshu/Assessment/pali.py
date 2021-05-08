a = input("enter the string: ")
def Pal(a):
    return a == a[::-1]
ans = Pal(a)
if ans:
    print("is Palindrome")
else:
    print("not palindrome ")
