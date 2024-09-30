def Search2D(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==target:
                return True
            
    return False

arr  = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 10
print(Search2D(arr, target))