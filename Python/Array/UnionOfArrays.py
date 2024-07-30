def UnionOfArray(arr1,arr2):
    return list(set(arr1) | set(arr2))

arr1 = [1,2,3,4,5,6]
arr2 = [5,6,7,8,9]
print(UnionOfArray(arr1,arr2))