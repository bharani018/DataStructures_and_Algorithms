def SecondLargest(arr):
    first= second = float('-inf')
    for i in arr:
        if(i>first):
            second = first
            first = i
        elif (i> second and i!=first):
            second = i
    return second if second != float('-inf') else None 

arr = [3,5,9,8,2]
print(SecondLargest(arr))
            