def avgofAllSubarray(arr, k):
    n = len(arr)
    if n<k:
        return False
    avgArr = []
    avg1 = sum(arr[:k])
    avgArr.append(avg1/k)
    for i in range(k, n):
        
        avg1 +=  arr[i] - arr[i-k]
        avgArr.append(avg1/k)
    return avgArr



def sumAllSubArray(arr,k):
    newArr = arr[:k]
    Crsum = sum(newArr)
    res = []
    res.append(Crsum)
    for i in range(len(arr)):
        if(k+i<len(arr)):

            Crsum = Crsum - arr[i] + arr[k+i]
            res.append(Crsum)
    return res
arr = [1,2,3,4,5,6]
k = 3
print(sumAllSubArray(arr, k))
print(avgofAllSubarray(arr,k))
