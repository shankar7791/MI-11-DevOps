def accpt(input_string):

    input_string = input_string.replace(' ', ' ')

    input_string = input_string.lower()

    str = [input_string.count('a'), input_string.count('e'), input_string.count('i'), input_string.count('o'), input_string.count('u'), ]


    if str.count(0) > 0:
        print("No Vowels in the string ")
    else:
        print("All Vowels are present in the string ")
input_string = input("\nEnter the string : ")

accpt(input_string)