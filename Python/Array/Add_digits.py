def AddDigits(num):
    res = num
    a = 0
    temp = num
    
    if(num<10):
        return num
    else:
        ans = AddDigits(num%10 + AddDigits(num//10))
        return ans
    
num = 89
print(AddDigits(num))

def add(num):
    x = num 
    if(num<10):
        return num
    else:
        answer = add(num%10 + add(num//10))