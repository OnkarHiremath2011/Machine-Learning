# 4. Write a program to find whether a given username contains less than 10 
#    characters or not.
name =input("Enter your name: ")

length=0

for char in name:
    length+=1

    if length<10:
        print("The name contains less than 10  characters")
    else:
        print("The name contains more than 10  characters")