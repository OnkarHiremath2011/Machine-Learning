# WAP for multiplication table from user defined

n= int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    i+=1