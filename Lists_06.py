# LISTS TUPLES DICTIONARY SET ARE BUILT IN DATA TYPES...

# LISTS USE []

# ELEMENTS OF DIFFERENT DATA TYPES ARE ALSO ALLOWED

# INDEXING STARTS AT 0

# LISTS ARE MUTABLE

marks = [90,89,87,88,]
marks[0]=99
print(marks,'1')

# LIST SLICING IS SAME AS STRING SLICING
# LIST METHODS

marks.append(86) # ADDS ELEMENT AT THE END
print(marks,'2')
marks.sort()
print(marks,'3')
marks.sort(reverse=True)
print(marks,'4')
marks.reverse()
print(marks,'5')
marks.insert(0,100)
print(marks,'6')
marks.remove(99) # REMOVES THE FIRST OCCURENCE OF THE VALUE
print(marks)
marks.pop(2) # REMOVES THE ELEMENT AT THE INDEX
print(marks)

# movie=input("ENTER YOUR 1ST FAV MOVIE NAME \n")
# movie2=input("ENTER YOUR SECOND FAV MOVIE NAME \n")
# fav=[movie,movie2]
# print(type(fav),"\n",fav)

fav_movie=[]
fav_movie.append(input("enter your 1st fav movie\n"))
fav_movie.append(input("enter your 2nd fav movie\n"))
fav_movie.append(input("enter your 3rd fav movie\n"))
print(fav_movie)

# PALINDROME LIST

list=[1,2,1,3]
list1=list.copy()
list.reverse()
if(list==list1):
    print("yes")
else:
    print("not")
