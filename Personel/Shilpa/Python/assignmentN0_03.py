# Program 8 : Write a Python program to create the multiplication table of a number.
        # Sample output :
        # input a number: 6   
        # 6 x 1 = 6                                                              
        # 6 x 2 = 12                                                             
        # 6 x 3 = 18                                                             
        # 6 x 4 = 24                                                             
        # 6 x 5 = 30                                                             
        # 6 x 6 = 36                                                             
        # 6 x 7 = 42                                                             
        # 6 x 8 = 48                                                             
        # 6 x 9 = 54                                                             
        # 6 x 10 = 60
# for i in range(6,66,6):
#     print(i)


# Program 4 : Write a Python program to count the number of even and odd numbers from a series of numbers.
# user_series=int(input("please enter value:-"))
# c=0
# c1=0
# for i in range(0,user_series):
#         if i%2==0:
#                 c=c+1
#         else:
#                 c1=c1+1

# print("odd count:-",c1,"even count:-",c)


# Program 5 : Write a Python program to get the Fibonacci series between 0 to 50.
# def fibo(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return fibo(n-2)+fibo(n-1)


# for n in range(0,50):
#     print(fibo(n))

#Program 7 : Write a Python program that accepts a string and calculate the number of digits and letters.
# l1=['b','c','d','f','g','h','j','k','l''m','n','p','q','r','s','t','v','w''x','y','z','a','e','i','o','u']
# l2=["1","2","3","4","5","6","7","8","9","10"]
# c=0
# c1=0
# string=input("please enter the string which do u want to know how digit and how  many string are present:-")
# for i in string:
#     if i in l1:
#         c=c+1
# for i in string:
#     if i in l2:
#         c1=c1+1

# print("the total digit present in striong are",c)
# print("the total string present in striong are",c1)


# Program 3 : Write a Python program that accepts a word from the user and reverse it.
# user_input=input("please enter the string")
# print(user_input[::-1])



#   Program 2 : Write a Python program to construct the following pattern, using a nested while loop.
#         *
#         * *
#         * * *
#         * * * *
#         * * * * *
#         * * * *
#         * * *
#         * *
#         *

# for i in range(1,6):
#     print(i*"* ")
# for i in range(4,0,-1):
#     print(i*"* ")
'''Program 6 : Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of 
five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".'''
for i in range(1,50):
        if i%5==0 and i%3==0:
                print("FizzBuzzz")
        else:
                print("Buzzz")






