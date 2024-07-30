
def Duplicate(arr):
    seen = []
    duplicate = []
    for i in arr:
        if i in seen:
            duplicate.append(i)
        else:
            seen.append(i)
    return duplicate

arr = [1,2,3,1,1,4,4,5]
print(Duplicate(arr))
