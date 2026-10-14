#  SET is the colection of unordered iteams
#  Each element in SET must be unique, non-repeatable and immutable
# we can store int,float,string,tuple etc. 
# ->but cannot store list and dictionary bcz they consist mutable element

# SET is mutable -> u can add or remove etc.
# elements in SET are Immuatble -> u cannot change existing element


sett= set()         # empty set
print(type(sett))

collection ={1,2,7,44,2,2,2,2,"name",(1,2,55)}
print(type(collection))
print(collection)                               #it is unordered

print(len(collection))