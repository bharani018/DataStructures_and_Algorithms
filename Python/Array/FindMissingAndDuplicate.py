def MissingAndDuplicates(arr):
    seen = []
    duplicate = []
    for i in arr:
        if i in seen:
            duplicate.append(i)
        else:
            seen.append(i)

    dupSum = sum(duplicate)
    arrSum = sum(arr)
    maxEle = max(arr)
    total = (maxEle*(maxEle+1))/2
    MissingElement = total - (arrSum-dupSum)
    return MissingElement, duplicate




arr = [1,2,2,4]
missing, duplicate = MissingAndDuplicates(arr)
print(missing)
print(duplicate)