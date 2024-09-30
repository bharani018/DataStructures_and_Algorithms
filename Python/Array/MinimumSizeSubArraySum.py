#leetcode 209

def MinSizeSubArraySum(arr, t):
    k=1
    n=len(arr)
    count = 0
    

    if t in arr:
        count = 1
    crSum = sum(arr[:k])
    for i in range(k, n):
        if crSum == t:
            count = k 
        else:
            
        
nums = [2,3,1,2,4,3]