def RotateArray(arr,k):
    
    x=[]
    y = []
    n = len(arr)
    
    c=0
    for i in range(len(arr)-1,1,-1):
        x.append(arr[i])
        c+=1
        if(c==k):
            break
    for j in range(0,len(arr)-k):
        y.append(arr[j])
    a = x[::-1]
    for i in y:
        a.append(i)
    return a
arr = [1,2,3,4,5,6]
k = 2
print(RotateArray(arr,k))