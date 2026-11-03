# default arguement is a default value eg.

def average(a=4,b=6):   #default values are a=4 & b=6
    avg=((a+b)/2)
    return avg

print(average())    # default a=4 & b=6

print(average(6))   # a=6(user defined) & b=6(b is default)

print(average(b=2)) # a=6(a=default) & b=2(user defined)

print(average(7,5)) # a=7 & b=5 (both user defined)


def FullName(sname="Onkar", mname=" Shivanand", lname=" Hiremath"):
    name=sname+mname+lname
    return name
print(FullName())

print(FullName(sname="python",mname=" Onkar"))

print(FullName("Kiran"))

print(FullName("Siddharam"," Shantling"))

print(FullName(sname="Kaveri", lname=" Chadchankar"))
