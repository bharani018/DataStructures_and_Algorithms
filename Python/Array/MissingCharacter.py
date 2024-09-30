def MissingChar(a):
    
    j = -1
    i=0
    n = len(a)
    new = ''
    while (i<n):
        if(a[i] == a[j]):
            new+=''
        else:
            new+=a[i]
        i+=1
        j-=1
    if(len(new)!=0):
        return new
    else:
        return "No String"

a = "abcdfjlkcba"
print(MissingChar(a))