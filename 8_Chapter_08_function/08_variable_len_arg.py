#  It allow a function to accept an arbitary no. of arguements to function

# 1. *args (tuple)
def add(*args):
    total = 0
    for num in args:
        total += num
        print('the sum is: ',total)
        return total
    
print(add(9,7))


# 2. Dictionary
def Name(**name):
    for key, value in name.iteams():
        print(f"{key}: {value}")

print(Name(name="Onkar", age=20))