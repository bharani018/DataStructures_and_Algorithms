def FindDplicates(arr):
    seen = []
    dplicate = []
    cnt = 0
    for i in arr:
        if(i in seen):
            dplicate.append(i)
        else:
            seen.append(i)
    return dplicate
arr = [1,2,2,4,5,1]
print(FindDplicates(arr))
