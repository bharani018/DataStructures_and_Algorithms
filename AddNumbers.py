def sortList(head):
    for i in range(len(head)):
        for j in range(i+1, len(head)):
            if(head[i]>head[j]):
                head[i], head[j] = head[j], head[i]
    return head

head = [4,3,2,1]
print(sortList(head))