def MinTiles(arr, n):
    l = len(arr)
    arr.sort(reverse=True)
    c = 0
    i = 0
    new = []
    while n>0:
        while i<l and arr[i]>n:
            i+=1
        if i<l:
            c += n//arr[i]
            x = n//arr[i]
            new.extend([arr[i]]*x)
            
            n %=arr[i]
        else:
            break
    return new,c

arr = [1,5,10]
n =27
a,tiles = MinTiles(arr,n)
print(a)
print("Tiles: ",tiles)

def MinTiles(arr, k):
    arr.sort(reverse= True)
    i=0
    res = []
    while k>=0 and i<len(arr):
        if(k>=arr[i]):
            
            res.append(arr[i])
            k -=arr[i]
        else:
            i+=1
    return res, len(res)

arr = [10, 5, 1]
k = 26
til, req = MinTiles(arr, k)
print(til)
print(req)