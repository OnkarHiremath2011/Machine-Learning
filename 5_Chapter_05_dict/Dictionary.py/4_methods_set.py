hulk = set()
hulk.add(3)
hulk.add(6)
hulk.add(2)
hulk.add(3)
hulk.add("my fault")
hulk.add((5,7,24,6,9.6,100.99))
# # hulk.add([7,"kasino",None])       #error -> list

print(hulk)

hulk.remove(3)
print(hulk)

# hulk.remove(668)              #error -> element does not exist in set
# print(hulk)

print(hulk.pop())
print(hulk.pop())
print(hulk)

print(hulk.clear())