def rem_set(s) :
    while s :
        s.pop()
        print(s)

user_set = set([12,13,45,86,7,919,54,15,8])
print(f"Set is : {user_set}")
print("Removing items from set until set becomes empty")
rem_set(user_set)