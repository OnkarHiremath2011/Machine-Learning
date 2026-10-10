#  f-string
name = "Onkar"
surname = "Hiremath"
print(f"Hello, I am {name} {surname}")
print("Hi {}".format(name))

x = "encyclopedia"

print(len(x))                     #length of string
print(x.endswith("pedia"))        #checks the end element
print(x[-1])

print(x.startswith("encyclo"))    #checks the first element
print(x[0])

print(x.capitalize())             #capitalize the first word
print(x.upper())                  #all words in capital
print(x.lower())                  #all words in small

str2 ="the greatest of all time"    #Starts each word with capital letter
print(str2.title())

print(x*3)                        #string repeatation

# search and replace
s = "I like Python"
print(s.find("like"))
print(s.replace("like","love"))

# spliting the string 
sq = "apple,cherry,chikoo"
print(sq.split(" "))

# splitting the string
sa = "    python   "
print(sa.split())

# character to ASCII value 
print(ord("A"))

# ASCII value to character
print(chr(97))

# string converting
piz = str(234)
print(piz)

