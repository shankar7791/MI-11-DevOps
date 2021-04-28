import string
alphabet = set(string.ascii_lowercase)
def ispan(string):
    return set(string.lower()) >= alphabet
string = "the quick brown fox jumps over the lazy dog"
if(ispan(string) == True):
    print("yes")
else:
    print("no")