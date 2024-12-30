# 8)Nexted if:

# Get the Electrycity UNIT from user.
#   if unit is upto 199----charge is 1.20 Rs
#   if unit is 200 and above but less than 400----charge is 1.50 Rs
#   if unit is 400 and above but less than 600----charge is 1.80 Rs
#   if unit is 600 and above ----charge is 2.00 Rs.

# find bill.
# suppose bill exceed RS. 400 the subcharge of 15% will be charged and minimum bill be should be RS. 100

# ex:
# input unit:300
# output:3450

a=float(input("Enter your electricity unit : "))
b=0
if a<=199:
    b=a*1.20
if a>=200 and a<400:
    b=a*1.50
elif a>=400 and a<600:
    b=a*1.80
elif a>=600:
    b=a*1.80
if b>400:
    c=b*0.15
    b=b+c
else:
    b=b
if b<100:
    b=100
print("your electricity bill is Rs.",b)