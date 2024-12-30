# 6)get the name,rollnumber,tamil, eng, maths mark from user.
#   if 3 subject total is greater than 90, output will be First class.
#   if 3 subject total is greater than 80, output will be Second class.
#   if 3 subject total is greater than 60, output will be third class.
#   if 3 subject total is greater  than or equal to 35, output will be Avarage.
#   otherwise fail.

a=input("Enter your name : ")
b=int(input("Enter your rollnumber : "))
c=int(input("Enter your mark in Tamil : "))
d=int(input("Enter your mark in English : "))
e=int(input("Enter your mark in Maths : "))
Total=c+d+e
Average=Total/3
if Average>90:
    print(a,"rollno",b,"You are passed in First Class")
elif Average>80:
    print(a,"rollno",b,"You are passed in Second Class")
elif Average>60:
    print(a,"rollno",b,"You are passed in Third Class")
elif Average>=35:
    print(a,"rollno",b,"You are passed in Average")
else:
    print(a,"rollno",b,"You are Fail")