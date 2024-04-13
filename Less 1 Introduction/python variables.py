# Multi word variable names
myVariableName = "Camel Case"
MyVariableName = "Pascal Casa"
_myVariableName = "Snake case"
print(' ')
print(myVariableName)
print(' ')
print(MyVariableName)
print('')
print(_myVariableName)
print('')

#Assign many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print(' ')

#Assign one values to multiple variables
x = y = z = "Banana"
print(x)
print(y)
print(z)
print('')

#Unpack a collection
fruits = ["Banana", "Apple", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print('')

#Output multiple variables, separated by a comma: It is recommended one
x = "Python"
y = "is"
z = "interesting"
print(x, y, z)
print(' ')

#You can also use the '+' operator to output multiple variables:
print(x + y + z)
print(' ')
