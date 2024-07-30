
def TwoSUM(arr, target):
    arr.sort()
    first, end = 0, len(arr)-1
    while first<end:
        crnt_Sm = arr[first] + arr[end]
        if(crnt_Sm == target):
            return (arr[first], arr[end])
        elif(crnt_Sm < target):
            first+=1
        else:
            end-=1
    return None
arr = [4,2,6,1,5,9]
target = 7

print(TwoSUM(arr, target))

