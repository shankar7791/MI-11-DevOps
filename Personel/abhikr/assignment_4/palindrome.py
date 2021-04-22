#prog 4.3. Write a Python program to reverse the digits of a given number and add it to the original, 
# If the sum is not a palindrome repeat this procedure.

a=int(input("Enter input one: "))

def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n 

print(rev_number(a))