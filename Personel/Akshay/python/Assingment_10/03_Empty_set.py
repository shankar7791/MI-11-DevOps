# emove items from Set until set not become empty set
def remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)
initial_set = set([1,2,3,4,5,6,7])
remove(initial_set)