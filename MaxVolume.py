def Area(x,y):
    area = x*y
    return area

def MaxVolume(height):
    maxArea = 0 
    
    for x in range (len(height)):
        for y in range(x+1, len(height)):
            z = min(height[x],height[y])
            a = Area(z,(y-x))
            maxArea = max(maxArea,a)
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(MaxVolume(height))
