def sortList(head):
    for i in range(len(head)):
        for j in range(i+1, len(head)):
            if(head[i]>head[j]):
                head[i], head[j] = head[j], head[i]
    return head

head = [4,3,2,1]
print(sortList(head))

def addNumbers(head):
    x = []
    num = head
    b = head
    while b>10:
        num = b
        b=0
        while num>0:
            a = num%10
            b+=a
            num//=10
            
    return b
head = 1239
print(addNumbers(head))
