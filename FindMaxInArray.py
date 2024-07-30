def MaxEle(arr):
    max = arr[0]

    for i in arr:
        if i>max:
            max = i
    
    return (max)

arr = [3,6,2,7,9,23]
print(MaxEle(arr))


