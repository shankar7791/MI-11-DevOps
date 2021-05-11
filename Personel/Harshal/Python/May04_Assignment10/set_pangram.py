def check_pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str:
            return False
  
    return True

string = input("Enter a String : ")
string = string.lower()
string = set(string)
if(check_pangram(string) == True):
    print("Entered String is pangram")
else:
    print("Entered String is not pangram")