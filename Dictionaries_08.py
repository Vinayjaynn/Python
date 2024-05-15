# DICT ARE STORED IN KEY : VALUE PAIRS

# DICT USE CURLY  BRACKETS ' {} '

# VALUES CAN BE OF ANY DATA TYPES

# KEY SHOULD BE ALWAYS IMMUTABLE VALUE " TUPLES , INT , STRING ETC "

# DICT ARE MUTABLE AND UNORDERED( NO INDEX ) AND NO DUPLICATE KEYS AS IN REAL LIFE DICTIONARY

# VALUES CAN BE ACCESSED BY ITS KEY

info = {
    "name":"Vinay",
    "age":21,
    "height":171.90,
    "college":"Christ",
    "is_adult":True,
    "subjects":["chem","phy","maths"],  
    "marks":{                   # NESTED DICTIONARY
        "chem":19,
        "phy":20,
        "maths":21      
    }
}

print(info)
print(info["name"])
print(info["age"])
print(info["college"])
print(info["subjects"])
print(info["marks"]["maths"])

# METHODS IN DICT

print(info.keys())
print(list(info.keys()))
print(tuple(info.keys()))
print(len(info)) # TOTAL NO OF OUTER KEY VALUE PAIRS


print(list(info.values()))
print(tuple(info.values()))

print(list(info.items()))   # EVERY PAIR IS RESULTED AS TUPLE WHOLE IS RESULTED AS LIST
print(type(info))

new=list(info.items())
print(new)
print(new[0])
new.insert(0,("a","A"))
print(new)

# THERE ARE TWO WAYS TO GET A VALUE 

print(info["name"])
print(info.get("name"))

""" 
THE MAJOR DIFFERENCE IS IF WE PASS ANY KEY WHICH DOESN'T EVEN EXIST THEN
THE FIRST DIRECT ACCESSING OF KEY WILL RESULT IN AN ERROR
BUT THE SECOND " GET FUNCTION " WONT GIVE AN ERROR INSTEAD WILL GIVE NONE AS OUTPUT
"""
# print(info["nameeee"])    --> Error
print(info.get("nameee")) # --> None

info.update({"city":"Banglore","age":22})
print(info.items())