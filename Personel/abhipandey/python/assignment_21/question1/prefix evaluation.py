
def is_operand(c):
    
	return c.isdigit()


def evaluate(expression):
	
	stack = []

	for c in expression[::-1]:

		if is_operand(c):
			stack.append(int(c))

		else:
			
			x = stack.pop()
			y = stack.pop()

			if c == '+':
				stack.append(x + y)

			elif c == '-':
				stack.append(x - y)

			elif c == '*':
				stack.append(x * y)

			elif c == '/':
				stack.append(x / y)

	return stack.pop()

if __name__ == "__main__":
	test_expression = "9+7*28"
	print(evaluate(test_expression))



