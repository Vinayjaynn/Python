a=2
b=3
c="#"
d=10
e=5.0
f=5
print(a*b*c)
print(a*e)
#print(a*e*c) not possible
#print(c+(a*b)) not possible
#print(a+c) NOT POSSIBLE
print(d/f,'1') # NORMAL DIVISION ALWAYS RESULTS IN FLOAT 
print(10.0//f,'2') # FLOOR DIVISION RESULT DEPENDS ON INPUT , DEFAULT IT RESULTS IN INT
print(d//f,'3')
print(d//3, '4') # FLOOR DIVISION JUST PRINTS THE CLOSEST INTEGER WHICH IS LESSER OR EQUAL TO THE ANS
print(d/3,'5')
print(10.0%3,'6') # MODULO JUST PRINTS THE REMAINDER RETURN TYPE SAME AS FLOOR DIVISION
print(d%2,'7')
print(d//-3,'8')
print(-10//3,'9')
print(-10//-3,'10')
"""IN MODULO IF BOTH NUMERATOR AND DENOMINATOR SIGN ARE SAME 
   THEN NORMAL MODULO REMAINDER WITH SAME SIGN OF DENOMINATOR
   ELSE NUMERATOR AND DENOMINATOR HAVE DIFF SIGN THEN
   FINAL ANSWER WILL BE REVERSE MODULO (LET CASE:3 ,IF ANS SHLD BE 1 , REV MOD ANS = 2)
   WITH SIGN OF DENOMINATOR"""
print(10%3,'8')
print(10%-3,'9') 
print(-10%3,'10') 
print(-10 % -3,'11')


name=input("PLEASE ENTER YOUR NAME : \n")
age=int(input("PLEASE ENTER YOUR AGE : \n"))
height=float(input("PLEASE ENTER YOUR HEIGHT : \n"))
married=bool(input("PLEASE ENTER TRUE OR FALSE : \n"))
print(age*height)
print(married)

# OPERATOR PRECEDENCE NOT > AND > OR
print(not True and True or False)
print(not False or False and True)
print(not False or False and False)
print(False or not True and True)