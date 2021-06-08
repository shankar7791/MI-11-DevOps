def prefix(c):
	
	return c.isdigit()

def evaluate(expression):
	
	stack = []

	for c in expression[::-1]:

		if prefix(c):
			stack.append(int(c))

		else:
			o1 = stack.pop()
			o2 = stack.pop()

			if c == '+':
				stack.append(o1 + o2)

			elif c == '-':
				stack.append(o1 - o2)

			elif c == '*':
				stack.append(o1 * o2)

			elif c == '/':
				stack.append(o1 / o2)

	return stack.pop()

if __name__ == "__main__":
	test_expression = "+9*24"
	print("\nPrefix evaluation:",evaluate(test_expression))
print("\n")
