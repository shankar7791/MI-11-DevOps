def palindrome(string):
    
    string = string.lower()
    rev_str = reversed(string)

    if list(string) == list(rev_str):
       print("The string is a palindrome.")
    else:
       print("The string is not a palindrome.")
		
# Function to check whether the string is symmetrical or not		
def symmetry(a):
	
	n = len(a)
	flag = 0
	if n%2:
		mid = n//2 +1
	else:
		mid = n//2
		
	start1 = 0
	start2 = mid
	
	while(start1 < mid and start2 < n):
		
		if (a[start1]== a[start2]):
			start1 = start1 + 1
			start2 = start2 + 1
		else:
			flag = 1
			break
	if flag == 0:
		print("The entered string is symmetrical")
	else:
		print("The entered string is not symmetrical")
		

string = input("enter string:")
palindrome(string)
symmetry(string)

