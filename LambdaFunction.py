
#   LAMBDA FUNCTION IS AN ANONYMOUS FUNCTION. IT CAN TAKE N NUMBER OF ARGUMENTS BUT CAN TAKE ONLY ONE EXPRESSION
#    EXAMPLE: 

addition = lambda x, y: x+y
print(addition(3, 4))


def FunctionWithLambda(a):
    return lambda x : a+x

#   type 1 to pass parameters
new = FunctionWithLambda(2)
print(new(4))

#   type 2 to pass parameters
print(FunctionWithLambda(8)(9))

''' lambda, map, filter, reduce funcitons '''

#Example: map

my_lst = [1,2,3,4,5]

map_list = list(map(lambda x: x**2, my_lst))
print(map_list)

#   Example: filter

evenNumbers = list(filter(lambda x: x%2==0, my_lst))
print(evenNumbers)

#   example: reduce
from functools import reduce
reduceExample = reduce(lambda x, y: x+y, my_lst)
print(reduceExample)