class reverse_string:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(reverse_string().reverse_words(' Hello My Name Is Rahul'))

