# RECURSION :- WEHEN A FUNCTION CALLS ITSELF

def show(n):
    if(n==0):   # --> BASE CASE = WHERE SHOULD THE RECURSION STOP
        return  # --> RETURN STATEMENT WITHOUT ANY VALUE RETURNS THE CONTROL 
    print(n)
    show(n-1)

show(10)

# -------------------------------------------------------------

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
a=fact(5)
print(a)

# -------------------------------------------------------------

def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
    
b=sum(10)
print(b)

# -------------------------------------------------------------

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

lis=[100,101,102]
print_list(lis)

# -------------------------------------------------------------
