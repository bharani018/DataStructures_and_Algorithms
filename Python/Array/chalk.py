def Chalks(chalk, target):
    x = target
    temp = target
    c = 0
    while(target>=chalk[0]):
        i=0
        while(temp>=chalk[0] and i<len(chalk)):
            temp -= chalk[i]
            c+=chalk[i]
            i+=1
            
        target = temp
    return c
chalk = [3,4,1,2]
target = 25
print(Chalks(chalk,target))

