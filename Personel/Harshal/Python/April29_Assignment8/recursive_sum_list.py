def recursion(data_list) :
	sum = 0
	for i in data_list :
		if type(i) == type([]) :
			sum += recursion(i)
		else:
			sum += i

	return sum

list_data = [1, 2, [3, 4, 6], 5, [8, 10], [7, 9]]
print(f"List is : \n {list_data}")
print(f"Sum of items in list is {recursion(list_data)}")