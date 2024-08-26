
def ProductExceptSelf(arr):
    n = len(arr)
    left, right, result = [0]*n, [0]*n, [0]*n

    left[0] = 1
    
    for i in range(1,n):
        left[i] = left[i-1] * arr[i-1]
        
    
    right[n-1] = 1
    for i in range(n-2,-1,-1):
        right[i] =  arr[i+1] * right[i+1]

    

    for i in range(n):
        result[i] = left[i] * right[i]
    return result

   

arr = [1,2,3,4]
print(ProductExceptSelf(arr))
print([0]*3)