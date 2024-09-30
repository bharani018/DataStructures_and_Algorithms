'''
def TripletWithZeroSm(arr):
    arr.sort()
    triplets = []
    n = len(arr)
    for i in range(n-2):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = n-1
        while left<right:
            total = arr[i] + arr[left] + arr[right]
            if(total ==0):
                triplets.append([arr[i], arr[left], arr[right]])

                while left<right and arr[left] == arr[left+1]:
                    left+=1
                while left<right and arr[right] == arr[right-1]:
                    right-=1
                left+= 1
                right-=1
            
            elif (total<0):
                left+= 1
            else:
                right-=1
    return triplets

arr = [-1, 0, 1, 2, -1, -4]
print(TripletWithZeroSm(arr))
print(min([1,2,3]))
''''''else:
    diff = target - total
    diffi.append(diff)
    '''
def ClosestSum(nums,target):
    nums.sort()
    closeSum = float("inf")
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums) -1
        while left<right:
            total = nums[i] + nums[left] + nums[right]
            
            if(abs(total-target) < abs(closeSum-target)):
                closeSum = total
            if(total<target):
                left+=1
            elif(total>target):
                right-=1
            else:
                return total

nums = [-1,8,1,1,-4]
target = 1
print(ClosestSum(nums,target))