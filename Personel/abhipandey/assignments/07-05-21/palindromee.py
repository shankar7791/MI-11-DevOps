a = input(("enter the string: "))
def isPal(a):
    return a == a[::-1]
ans = isPal(a)
if ans:
    print("is Palindrome")
else:
    print("not palindrome ")