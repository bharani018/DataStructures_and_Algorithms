def MergedSortedArray(arr1,arr2):
    i,j = 0,0
    mergedArray = []
    while i<len(arr1) and j<len(arr2):
        if(arr1[i] < arr2[j]):
            mergedArray.append(arr1[i])
        else:
            mergedArray.append(arr2[j])
    while i<len(arr1):
        mergedArray.append(arr1[i])
        i+=1
    while j<len(arr2):
        mergedArray.append(arr2[j])
        j+=1
    return mergedArray

arr1 = [3,5,1,8,4]
arr2 = [2,7,6,9]
print(MergedSortedArray(arr1,arr2))