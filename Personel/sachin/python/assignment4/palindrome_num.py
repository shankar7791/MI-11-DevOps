def rev_number(n):
  num = 0
  while True:
    val = str(n)
    if val == val[::-1]:
      break
    else:
      rev = int(val[::-1])
      n += rev
      num += 1
  return n 

num = int(input("Enter a Number : "))
a = str(num) 
reverse = (a[::-1]) 
pelindrome = rev_number(num)
print(f"Reverse of {num} is {reverse} & Palindrome number is {pelindrome}")