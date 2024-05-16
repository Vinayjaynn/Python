# # Functions : 
# # Block of statements to perform any task n number of times
# # Main use of functions is to reduce the redundancy of the code

# n=int(input("Enter the no of subjects you want to calculate the average\n"))
# # a=int(input("Enter the marks"))
# # b=int(input("Enter the marks"))
# # c=int(input("Enter the marks"))
# i=0
# li=[]
# while i<n:
#     li.insert(i,int(input("Enter")))
#     i+=1
# print(li)



# def avg(a,b,c):
#     average=(a+b+c)/3
#     print(average)

# avg(li[0],li[1],li[2])

num=[1,2,3,4,5,6,7]

def length(num):
    print(len(num))

length(num)


def print_list(num):
    for i in num:
        print(i,end=" ")

print_list(num)
print()



def fact_(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

fact_(5)


def conversion(n):
    print("USD = ",n)
    print("INR = ",n*80)

conversion(5)

def check(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

x=int(input("Enter a number \n"))
check(x)