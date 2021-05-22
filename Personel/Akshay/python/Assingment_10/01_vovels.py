# Program to accept the strings which contains all vowels
def remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)
initial_set = set([2,3,4,5,6,7])
remove(initial_set)