def add (a,b):
    return a + b
def subtract (a,b):
    return a - b
def multiply (a,b):
    return a * b
def divide (a,b):
    if b != 0:
        return a / b
    return "Can't divide by 0"

#Here I created a dictionary to link the operators with the funcions, so we can call them later
operators = {

    '+': add, #Function
    '-': subtract,
    '*': multiply,
    '/': divide,

}

operation = input("Input your operation here: ")

operation = operation.split() #Divide the STR and turn to a list () -> means it will split with the default mode "every space"
elements = list(filter(bool, operation)) #Create a List with every element in the operation, used the function filter with BOOL because when it's " " it will return false and not be filtered, removing spaces

if len(elements) == 3:
    n1 = int(elements[0])
    n2 = int(elements[2])
    operator = elements[1]

    if operator in operators:
        result = operators[operator](n1,n2) #Calling the dictionary, for example divide, then it will be divide(n1, n2) the function already with the arguments
        print (float((result)))

