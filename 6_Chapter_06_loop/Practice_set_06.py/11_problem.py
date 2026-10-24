# Write a program to find whether a given number is prime or not

n=int(input('Enter the number: '))

for i in range(2,n):
    if(n%i==0):
        print('It is not Prime number')
        break
    else:
        print('It is Prime number')
i+=1