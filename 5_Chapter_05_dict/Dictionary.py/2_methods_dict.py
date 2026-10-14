dict = {
    "Name":"Onkaar",
    "Age" : 20,
    "Marks": "100",
    list : [23,5,60,20]
  
}
# 1
print(dict.items())

  # 2
print(dict.keys())

 # 3
print(dict.values())

# 4
value = dict.pop("Age")     # Removes the key and returns its value
print(value)
print(dict)

 # 5
pair = dict.popitem()   #Removes last inserted item & returns a key-value pair as a tuple
print(pair)
print(dict)

  # 6
dict.setdefault("marks",78)  #Returns the value for the specified key. 
print(dict)                 #If the key does not exist, inserts it with the specified default value
      
                
  # 7
dict.update({"Name":"Onkar", "Surname":"Hiremath"})
print(dict)

    # 8
copy = dict.copy()      # Gives a shallow copy of dict
print(copy)

  # 9
# Following both the methods are diferent 
# Both will give same output now 
print(dict.get("Name")) #Onkar
print(dict["Name"])     #Onkar

   # 10A
# But If we use it when the key is not in dictionary then it will return as :
print(dict.get("Name2"))   # prints NONE
print(dict["Name2"])       # Error

# 10B
print("Before !")
print(dict.["man"])         #it gives error and programs stops executing
print("After !")

# 10C
print("Before !")
print(dict.get("man"))          #it doesn't gives any error and program executes easily
print("After !")                # hence methods are used


  # 11
dict.clear()
print(dict)