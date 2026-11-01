# 5. Write a program which finds out whether a given name is present in a list or not.

list=['onkar','venku','avinash','manikanth','vishal','atharva','balaji','kiran','appu','sagar']

name = input("Enter name you want to find: ")

if name in list:
    print(f"{name} name exist in this list")
else:
    print(f"{name} name does not exist in this list")
