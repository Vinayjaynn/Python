# SET CONTAINS UNIQUE VALUES AND IS 

# SET IS A MUTABLE BUT ELEMENTS OF THE SET ARE IMMUTABLE 

# TATS Y LIST AND DICT CANNOT BE INSIDE SET

# SET ALSO USES ' {} '

# SET CAN CONTAIN ANY DATA TYPES EXCEPT LIST AND TUPLE CUZ THEY BOTH ARE MUTABLE

# SET IS UNORDERED AND DUPLICATES VALUE GETS IGNORED

collection={1,2,2}
print(type(collection))
print(collection)
print(len(collection))

collection={} # EMPTY DICT
print(type(collection))

collection=set() # EMPTY SET
print(type(collection))

collection.add(1)
print(collection)
collection.remove(1)
print(collection)
collection.add("We can pass a string , tuple anything here")
collection.add("we cannot add list and dict cuz they are unhashable --> mutable ")
collection.add("vinay")
collection.add("vinit")
collection.add("ankit")
collection.add("gaurav")
print(len(collection))

print(collection.pop()) # --> pops any random value

set1={9,9.0}
print(set1)

# set1.union(set2)
# set1.intersection(set2)

values={
    ("float",9.0),
    ("int",9)
}

print(values)
