def Intersection(arr1,arr2):
    reslt = []
    for i in arr1:
        if i in arr2:
            reslt.append(i)
    return reslt

def IntersectionMethod2(arr1,arr2):
    #Using and operator and list and set
    return list(set(arr1) & set(arr2))
    
arr1 = [1,2,3,4]
arr2 = [3,4,5,6]
print(Intersection(arr1,arr2))
print(IntersectionMethod2(arr1,arr2))