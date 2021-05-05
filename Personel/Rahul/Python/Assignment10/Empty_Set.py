def remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)
initial_set = set([1,3,5,7,2,4])
remove(initial_set)