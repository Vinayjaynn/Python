# if , if-elif , if-elif-elif , if-elif-else , if-else 

light = input("PLEASE ENTER THE COLOR OF THE LIGHT \n")
if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("GET READY")
elif(light == "green"):
    print("GO")
else:
    print("PLEASE ENTER THE CORRECT LIGHT COLOR")



marks = int(input("PLEASE ENTER YOUR MARKS\n"))
if (marks>=90 and marks<100):
    print("A GRADE")
elif(marks>=80 and marks < 90):
    print("B GRADE")



age = int(input("PLEASE ENTER YOUR AGE\n"))
gender = input("PLEASE ENTER M OR F \n")
if(age < 18 and gender == "F"):
    print("YOU ARE A BABY GIRL\n")
elif(age<18 and gender =="M"):
    print("YOU ARE A SMALL BOY")
elif(age>18 or gender =="M" or gender=="F"):
    print("YOU ARE AN ADULT")
else:
    print("PLEASE ENTER THE DETAILS CORRECTLY \n")

# TERNARY OPERATORS

eligibility = "yes you are eligible to vote" if age>18 else "no you are not eligible to vote"
print(eligibility)

print("you are eligible to drive") if age>18 else print("no you cannot drive ")

# CLEVER IF TERNARY OPERATOR
# ( "FALSE VAL" , "TRUE VALUE" ) [ IF CONDITION ]   -> CLEVER IF SYNTAX
eat=("yes you can eat","no you are still underage to eat")[age<3]
print(eat)