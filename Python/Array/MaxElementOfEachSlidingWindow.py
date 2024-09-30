def MaxElementOfEachSlidingWindow(arr, k):
    n = len(arr)
    if n<k:
        return False
    
    
    MaxArr = []
    
    for i in range(n):
        if((k+i)<n+1):
            newArr = arr[i:k+i]
            MaxArr.append(max(newArr))
    return MaxArr
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k=3
print(MaxElementOfEachSlidingWindow(arr, k))