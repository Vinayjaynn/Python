# f=open("Print_01.py", "r")
# data=f.readline()
# content = f.read()
# print(data)
# print(content)
# f.close()

# Diff modes
# r , w , a , r+ , w+ , a+

# To delete any file
# import os 
# os.remove("filename")

# f = open("practice.txt","a+")
# f.write("hi everyone \n we are learning java \n with apna college \n i like programming in java\n")
# f.close()
# f = open("practice.txt")
# data=f.read()
# new_data=data.replace("java","python")
# print(new_data)
# print(data.find('h'))

f = open("practice.txt","r")
data=f.read()
lists = data.split(",")
print(lists)
count = 0
for i in lists:
    if(int(i)%2==0):
        count+=1
    else:
        pass
print(count)

