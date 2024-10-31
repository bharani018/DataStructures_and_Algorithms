

#PYTHON DO NOT USE CALL BY VALUE OR CALL BY REFERENCE INSTEAD IT USES CALL BY OBJECT REFERENCES OR (CALL BY ASSIGNMENT)

# IMMUTABLE OBJECTS: INT, FLOAT, STRING, TUPLE. IN THE CASE OF IMMUTABLE OBJECTS PYTHON ACTS LIKE CALL BY VALUE. i.e THE VALUES OF THE OBJECT ARE NOT AFFECTED
# MUTABLE OBJECTS: LIST, ARRAY, DICTIONARY ETC.. IN THE CASE OF MUTABLE OBJECTS PYTHON ACTS LIKE CALL BY REFERENCE.. i.E. THE VALUES OF THE OBJECTS DECLARED OUTSIDE THE METHOD ARE AFFECTED WHEN CALLED INSIDE THE METHOD

#   call by value Example:

def CallByValue(value):
    total  = value + 10

    return f'Inside the function: {total}'

value = 10
print(CallByValue(value))
print("Outside fuction: ", value)


#   call by reference Example:

def CallByReference(list):
    list.append(2)
    return f'Inside function: {list}'

my_list = [1, 3, 4, 5]
print(CallByReference(my_list))
print('Outside function: ', my_list)
