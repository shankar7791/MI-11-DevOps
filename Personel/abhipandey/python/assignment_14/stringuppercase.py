class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    print("Enter String -")
    def print_String(self):
        print("String in Upper case -")
        print(self.str1.upper())
        
        
str1 = IOString()
str1.get_String()
str1.print_String()