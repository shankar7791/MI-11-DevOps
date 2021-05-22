def max_product(arr) :
    arr_len = len(arr)
    if (arr_len < 2) :
        return("No pairs exists")
    x = arr[0]; y = arr[1]

    for i in range(0, arr_len) :
        for j in range(i + 1, arr_len) :
            if (arr[i] * arr[j] > x * y) :
                x = arr[i]; y = arr[j]
    return x,y

number = [1, 2, 3, 4, 7, 0, 8, 4]
print("Array 1 :",number)
print("Maximum product pair is : ", max_product(number))

number = [0, -1, -2, -4, 5, 0, -6]
print("Array 2:",number)
print("Maximum product pair is : ", max_product(number))