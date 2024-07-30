
def Duplicate(arr):
    seen = set()
    duplicate = set()
    for i in arr:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    return duplicate

arr = [1,2,3,1,1,4,4,5]
print(Duplicate(arr))
