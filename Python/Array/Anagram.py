from collections import Counter
def Anagram(str, new):
    a = Counter(str)
    b = Counter(new)
    if(a==b):
        return True
    return False
    
str = "aacc"
new = "ccaa"
print(Anagram(str, new))