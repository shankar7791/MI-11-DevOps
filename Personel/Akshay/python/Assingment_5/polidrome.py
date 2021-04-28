
#Python program create function to check if a string is palindrome or not
my_str = 'radar'
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is a Palindrome ")
else:
    print("The string is not a Palindrome ")
