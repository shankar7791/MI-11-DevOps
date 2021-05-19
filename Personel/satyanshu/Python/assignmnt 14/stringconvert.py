
class convert():
    def __init__(self):
        self.stri = ""

    def get_String(self):
        self.stri = input("Enter a string : ")

    def print_String(self):
        print("String in upper case : ")
        print(self.stri.upper())
        
        
stri = convert()
stri.get_String()
stri.print_String()
