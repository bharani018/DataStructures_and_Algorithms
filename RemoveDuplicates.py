def RemoveDUplicates(arr):
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    return new

arr = [4,2,2,1,5,2,6,7,4]
print(RemoveDUplicates(arr))