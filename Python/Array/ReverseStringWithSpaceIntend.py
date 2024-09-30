
def ReverseString(a):
    
    n = len(a)
    new = [0]*n
    for i in range (n):
        if(a[i] == ' '):
            new[i] = ' '
    j = -1
    for i in range(len(a)):
        if (a[i]!= ' '):
            if (new[j] == ' '):
                j-=1
            new[j] = a[i]
            j-=1
    return ''.join(new)


 
a = "a bc"
b = "abscxad"
print(ReverseString(a))
