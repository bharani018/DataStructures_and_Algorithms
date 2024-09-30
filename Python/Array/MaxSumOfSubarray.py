def MaxSumOfSubarry(arr,k):
    n = len(arr)
    if n<k:
        return False 
    else:
        currentSum = maxSum = sum(arr[:k])

        for i in range(k, n):
            currentSum += arr[i] - arr[i-k]
            maxSum = max(currentSum, maxSum)
    return maxSum

arr = [1,2,5,1,3,2]
k=3
print(MaxSumOfSubarry(arr,k))