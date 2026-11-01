# 1 Write a program to find the greatest of four numbers entered by the user. 
a=int(input('Enter 1st numbers: '))
b=int(input('Enter 2nd numbers: '))
c=int(input('Enter 3rd numbers: '))
d=int(input('Enter 4th numbers: '))

if(a>b and a>c and a>d):
    print("The greatest number is : ",a)

elif (b>a and b>c and b>d):
    print("The greatest number is : ",b)

elif(c>a and c>b and c>d):
    print("The greatest number is : ",c)

else:
    print("The greatest number is : ",d)