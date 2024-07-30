#FindMissingNmbers

def FindMissingNmbers(arr):
    maxi = max(arr)
    
    total = (maxi*(maxi+1))/2
    crntSm = 0
    for i in arr:
        crntSm +=i
    missed = total - crntSm
    return int(missed)

arr = [1,4,2,5]
print(FindMissingNmbers(arr))