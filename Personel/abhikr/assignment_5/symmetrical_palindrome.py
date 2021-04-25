#prog 5.3.: Python program to check
#  whether the string is Symmetrical or Palindrome.


my_str  = input("Input a string: ")


my_str = my_str.casefold()

rev_str = reversed(my_str)


if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


n = len(my_str)
flag = 0
     
if n%2:
    mid = n//2 +1
else:
    mid = n//2
          
start1 = 0
start2 = mid
      
while(start1 < mid and start2 < n):
          
    if (my_str[start1]== my_str[start2]):
        start1 = start1 + 1
        start2 = start2 + 1
    else:
        flag = 1
        break
       
   
if flag == 0:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")