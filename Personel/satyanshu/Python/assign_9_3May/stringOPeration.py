def length(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter

def reverse(str):
    return str[::-1] 

def palindrom(str):
    string = str.lower()
    rev_str = reversed(string)

    if list(string) == list(rev_str):
       print("The string is a palindrome.")
    else:
       print("The string is not a palindrome.")

def symmetrical(str):

	n = len(str)
	flag = 0
	if n%2:
		mid = n//2 +1
	else:
		mid = n//2
		
	start1 = 0
	start2 = mid
	
	while(start1 < mid and start2 < n):
		
		if (str[start1]== str[start2]):
			start1 = start1 + 1
			start2 = start2 + 1
		else:
			flag = 1
			break
	if flag == 0:
		print("The entered string is symmetrical")
	else:
		print("The entered string is not symmetrical")

def PermCombi(str):
    import itertools
    per = itertools.permutations(str)
    
    c=int(input("enter combination length : "))
    com = itertools.combinations(str, c)
    for val in com:
        print("combinations : ")
        print(*val)
    for val in per:
        print("permuations : ")
        print(*val)

def anagram(str1,str2):
    if(sorted(str2)== sorted(str2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")  

print("Select operation.")
print("1.Length of string")
print("2.Reverse String")
print("3.Check Palindrome or not")
print("4.Check Symmetrical or not")
print("5.Check Permutations and combination")
print("6.Check two strings are anagram or not")
print("7.Exit")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    if choice in ('1', '2', '3', '4'):
        str = input("Enter string: ")
        

        if choice == '1':
            print("Length of string : ", length(str))

        elif choice == '2':
            print("reverse string is : ", reverse(str))

        elif choice == '3':
            palindrom(str)

        elif choice == '4':
            symmetrical(str)
                    
        
    elif choice == '5':
        str=input("enter string : ")
        PermCombi(str)
    elif choice == '6':
        str1= input("enter first string : ")
        str2= input("enter second string : ")
        anagram(str1,str2)
    else:  
        exit()
