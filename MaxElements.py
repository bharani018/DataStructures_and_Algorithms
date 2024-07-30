def majorityElement(arr):
    maxCon = 0
    index = -1
    for i in range(len(arr)):
        con =0
        for j in range(len(arr)):
            if(arr[i] == arr[j]):
                con+=1
        
        if(con>maxCon):
            maxCon = con
            index = arr[i]
    if maxCon > len(arr) // 2:
        return majorityElement
    else:
        return "No majority element"


arr = [1,1,2,2,2,3,3,1,1,1,1,1,8]
print(majorityElement(arr))