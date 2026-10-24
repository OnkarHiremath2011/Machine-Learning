# take this tuple (1,4,9,16,25,36,49,64,81,100) and find 'x' number --> x = user input

# break 

tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter number you want to find: "))

i=0
while i<=len(tup):
    if(tup[i]==x):
        print("Number found at index ",i)
        break
    else:
        print("Number Not Found")
        i+=1