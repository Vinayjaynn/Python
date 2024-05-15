# OPERATIONS IN STRING
# 1. CONCATENATION - +
# 2. LENGTH - len(str) INDEXING STARTS FROM 1
# 3. STRING INDEX STARTS FROM 0 str[2] , str[0]
# 4. WE CANNOT MANIPULATE STRING USING ITS INDEX WE CAN JUST ACCESS THE STRING
# 5. STRING SLICING 
# 6. STRINGS ARE IMMUTABLE

str="vinay Jain"
print(str[1:5])
print(str[:5])  # same as str[0:5]
print(str[1:(len(str)-3)])  
print(str[1:])  # same as str[1:len(str)]

# NEGATIVE INDEXING
# DECREASES FROM RIGHT TO LEFT
print(str[-10:-1])
print(str[-5:-2])
print(str[:-2])
print(str[-9:])

print(str.endswith("n"))
print(str.endswith("Jain"))
print(str.capitalize())
print(str)
print(str.replace("i","a"))
print(str.replace("Jain","Gulecha"))
print(str.find("v"))
print(str.find("Vinay"))
print(str.find("vinay"))
print(str.count("a"))
print(str.count("vinay"))
print(str.count("i"))