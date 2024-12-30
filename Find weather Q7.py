# 7)Get the Temparature from user.
#   if tem greater than or equal to 0 and less than 10, output will be Very cold weather.
#   if tem greater than or equal to 10 and less than 20, output will be cold weather.
#   if tem greater than or equal to 20 and less than 30, output will be Normal Weather.
#   if tem greater than or equal to 30 and less than 40, output will be Hot.
#   otherwise Very hot.

a=int(input("Enter the Temperature of your area : "))
if a>=0 and a<10:
    print("The Weather is Very Cold")
elif a>=10 and a<20:
    print("The Weather is Cold")
elif a>=20 and a<30:
    print("The Weather is Normal")
elif a>=30 and a<40:
    print("The Weather is Hot")
else:
    print("The Weather is Very Hot")