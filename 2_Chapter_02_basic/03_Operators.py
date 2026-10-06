# OPERATORS IN PYTHON

# 1. Arithmetic operators: +, -, *, /,% etc. 
a = 8                   #operand 1
b = 3                   #operand 2
print("\nAddition is: ",a+b)
print("Substraction is: ",a-b)
print("Multipy is: ",a*b)
print("Square of b is: ",b**2)
print("Division is: ",a/b)
print("The modulo is: ",a%b) #Modulo operation % - gives Remainder 
print("5th power of a is: ",pow(a,5)) #pow() - Power , raise to
print("cube of b is: ",pow(b,3))


# 2. Assignment operators:  =, +=, -= etc.
x = 7
y = 8
print(x)
print(y)
y += 2                       #Add 2 in pre-existing value of y
print(y)
x -= 4                       #substract 4 in pre-existing value of x
print(x)


# 3. Comparison operators: ==, >, >=, <, <=, != etc. 
x == y                       #Check whether x = y
print(x==y)                  #If x = y it returns True ,If not returns False

x > y                        #If x > y returns True else False
print(x>y)

x >= y                        #If x > y returns True else False
print(x>=y)

x < y                        #If x < y returns True else False
print(x<y)

x <= y                        #If x <= y returns True else False
print(x<=y)

x != y                       #Check whether x != y               
print(x != y)                #If x != y it returns True ,If not returns False


# 4. Logical operators: and, or, not

# Truth table for "and"
print("\nTrue and False is: ",True and False)
print("True and True is: ",True and True)
print("False and True is: ",False and True)
print("False and False is: ",False and False)

# Truth table for "or"
print("\nTrue or False is: ",True or False)
print("True or True is: ",True or True)
print("False or True is: ",False or True)
print("False or False is: ",False or False)

# not operator             --- It makes  True -> False  &  False -> True
print(not(True))
print(not(False))