def VolumeTwoPointer(arr):
    i=0
    n=len(arr)
    j=n-1
     
    Maxarea = 0
    while(i<j):
        
        b = j-i
        l = min(arr[i], arr[j])
        area = l*b
        Maxarea = max(Maxarea, area)
        
        if(arr[i]<arr[j]):
            i+=1
        else:
            j-=1
    return Maxarea

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(VolumeTwoPointer(arr))