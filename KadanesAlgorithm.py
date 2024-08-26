def Kadane(arr):

    crntSm = GlobalMax = arr[0]
    for i in arr[1:]:
        crntSm = max(i, crntSm+i)
        GlobalMax = max(crntSm, GlobalMax)
        
            #return GlobalMax
    return GlobalMax

arr = [1, -3, 2, 1, 8, -1]
print(Kadane(arr))