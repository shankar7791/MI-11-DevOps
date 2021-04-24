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
final = rev_number(num)
print(f"Pallindrome number is {final}")