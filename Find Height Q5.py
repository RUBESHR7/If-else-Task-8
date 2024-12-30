# 5)Get the height from user.
#   if given height is less than 150, output will be small.
#   if given height is greater than or equal 150 and height less than 165, output will be Average Height.
#   if given height is greater than or equal 165 and height less than 195, output will be Taller.
#   otherwise output will be Abnormal height.-

a=int(input("Enter the number of your height : "))
if a<150:
    print("Your height",a,"is Small height.")
elif a>=150 and a<165:
    print("Your height",a,"is Average height.")
elif a>=165 and a<195:
    print("Your height",a,"is Taller height.")
else:
    print("Your height",a,"is Abnormal height.")