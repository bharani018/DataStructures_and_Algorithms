
def StockAnalysis(arr):
    buy = float("inf")
    sell = 0
    x = 0
    for i in arr:
        if(i<buy):
            buy = i
        elif(i-buy > sell):
            sell = i-buy
    return sell
    

     
arr = [5,4,6,3,6,5]
print(StockAnalysis(arr))