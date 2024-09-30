
#wrong
def plusOne(arr):
    temp = ''
    for i in arr:
        temp = temp+str(i)

    
    x = int(temp)+1
    x = str(x)
    new=[]
    for i in x:
        new.append(i)
    return new

arr = [1,2,4]
print(plusOne(arr))