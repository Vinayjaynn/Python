# WHILE LOOP
# while condition :
    # do this work
count = 1
while count <= 5 :
    print("hello")
    count+=1
# print(count)

nums = [1,4,9,16,25,36,39,64,81,100]
i = 0
while i<len(nums):
    print(nums[i], f"is at index {i}")
    i+=1

num = [1,4,9,16,25,36,39,64,81,100]
i = k = b = 0
while i<len(num):
    if num[i]==1:
        k=1;b=i
    i+=1
if(k==1):
    print("yes its there at index",b)
else:
    print("it is not there")

tupl=(1,2,3,4,5)
i=0
while i<len(tupl):
    if(tupl[i]==3):
        print("got it at ",i)
        break
    i+=1
    
tupl=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
i=0
while i<len(tupl):
    if(tupl[i]%2==0):
        i+=1
        continue
    print(tupl[i])
    i+=1

list1=[1,3,5,7,9,11,3]
idx=0
for val in list1:
    if(val==3):
        print("3 found at ",idx)
    idx+=1

# range(start? , stop , stepsize?)
# start = by default = 0
# stepsize by default = 1

for i in range(0,100,5):
    print(i)

for i in range(100,0,-1):
    print(i)

a=int(input("Enter a num \n"))
i=sum=0
while i<=a:
    sum+=i
    i+=1
print(sum)

fact=1
for i in range(1,a):
    # fact*=i
    a*=i
print(a)