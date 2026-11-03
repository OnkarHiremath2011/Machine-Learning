# Keyword Arguement

def FullName(sname="Onkar", mname=" Shivanand", lname=" Hiremath"):
    name=sname+mname+lname
    return name
# print(FullName())


# The sequence does not matter with arguements
print(FullName(lname=" Hiremath",sname="Onkar",mname=" Shivanand"))

# O\P =>Onkaar Onkar Hiremath 