l = [95, 28, 47, 31, 74, 41, 84, 40, 71, 84]
def even(list) :
    print ("Even number is :")
    for i in list :
        if (i % 2 == 0) :
            print (i ,end= " ")
    print()
even(l)