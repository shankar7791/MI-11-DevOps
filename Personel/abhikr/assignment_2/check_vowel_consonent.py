
#prog 2.5.Write a program to input any alphabets and check it is vowel or consonent


vowel=['a','e','i','o','u','A','E','I','O','U']
#consonent=['b','c','d','f','g','h','j','k','l''m','n','p','q','r','s','t','v','w''x','y','z']
alphabets=input(" Enter the alphabets:  ")
if alphabets in vowel:
    print("Alphabet is vowel ")
else:
    print("Alphabet is consonent ")

