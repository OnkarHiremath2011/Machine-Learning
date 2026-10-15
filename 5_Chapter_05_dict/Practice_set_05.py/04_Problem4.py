# figure out to store 9 & 9.0 in a same set
set1={9,9.5}
print(set1)

# BUT
set2={9,9.0}        # ->compiler treat them as same 9 & 9.0
print(set2)

# soln 1
set3={9,"9.0"}
print(set3)

# soln 2
set4={9.0,"9"}
print(set4)

# soln 3 imp ->create a tuple in set and mention their data types like
set5={
    ("int",9),
    ("float",9.0)
}
print(set5)