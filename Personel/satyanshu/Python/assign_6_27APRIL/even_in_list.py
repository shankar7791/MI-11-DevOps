list = map(int, input("enter numbers in list ").split())
def even_in_list(list):
    for num in list:
        if num % 2 == 0:
            print(num, end = " ")
even_in_list(list)            
       
