def string(words) :
    count = 0

    for i in words :
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    return count
print(string(['abc', 'xyz', 'aba', '1221']))
