num = int(input("Enter length of triangle : "))
def pascal_triangle(num):
	for i in range(num):
		print(" "*(num-i), end="  ")
		print(" ".join(map(str, str(11**i))))
pascal_triangle(num)

