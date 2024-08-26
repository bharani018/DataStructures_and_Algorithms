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
