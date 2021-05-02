n = int(input("Enter The Length Of Triangle : "))
def pascal_triangle(n):
	for i in range(n):
		print(" "*(n-i), end="  ")
		print(" ".join(map(str, str(11**i))))
pascal_triangle(n)

