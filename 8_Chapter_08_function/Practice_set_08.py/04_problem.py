# WAF to print the elements of list in single line (list the parameters)

names=['virat','rohit','msdhoni','rahul','pant',9,64,True]

def print_list(List):
    for iteam in List:
        print(iteam,end=" ")

print_list(names)


# print(names[1],end=" ")           #to print them in a same line we need to change function of print
# print(names[2],end=" ")
# print(names[3],end=" ")
# print(names[4],end=" ")
# print(names[5],end=" ")
# print(names[6],end=" ")
# print(names[7])
