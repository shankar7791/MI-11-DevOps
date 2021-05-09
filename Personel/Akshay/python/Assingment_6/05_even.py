# Write a Python program function to print the even numbers from a given list.
l = [80, 28, 7, 91, 4, 1, 8, 40, 71,]
def even(list) :
    print ("Even number is :")
    for i in list :
        if (i % 2 == 0) :
            print (i ,end= " ")
    print()
even(l)