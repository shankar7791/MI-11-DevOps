def list_fun(num_list):
    firstElement=num_list[0]
    lastElement = num_list[-1]
    if (firstElement == lastElement):
        return True

    else:
           return False


xlistx = [10, 20, 30, 20, 10]

print (list_fun(xlistx))