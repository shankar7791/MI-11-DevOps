class Reverse:
    def rev_word(self, s):
        return ' '.join(reversed(s.split()))

r = Reverse()
print("String is : hello my name is dev")
print("Reverse of string is \n", r.rev_word("hello my name is dev"))
