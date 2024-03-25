#Get user input
variable= input("Input here your Variable:")

#for every letter in variable
for c in variable:

    #if the letter is UPPERCASE we will print _ + letter, always ending with "" so we can create the whole variable by the end
    if c.isupper():
        print ("_" + c.lower(), end="")

    #Else just print the normal letter lower, ending with "" again
    else:
        print(c, end="")
print()

