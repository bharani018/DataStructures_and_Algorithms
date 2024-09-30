def MergeIntervals(arr):

    merged = []
    arr.sort(key=lambda x:x[0])
    prev = arr[0]
    for i in arr[1:]:
        if i[0]<=prev[1]:
            prev[1] = max(prev[1], i[1])
            
        else:
            merged.append(prev)
            prev = i
    merged.append(prev)
    return merged
        
        
        
arr = [[1,3],[2,6],[8,10],[15,18]]
print(MergeIntervals(arr))