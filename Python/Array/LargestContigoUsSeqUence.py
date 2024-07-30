
def LargestSeq(arr):
    longStreak = 0
    
    for i in arr:
        if i-1 not in arr:
            crntNm = i
            Seq = 1
            while crntNm+1 in arr:
                crntNm +=1
                Seq+=1
            longStreak = max(longStreak, Seq)
    return longStreak

arr = [29,32,42,30,25,31,32]
print(LargestSeq(arr))