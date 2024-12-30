# 2)a=[1,2,3,4,5,6,7,8].Find how many odd number and how many even number in the list?

a = [1, 2, 3, 4, 5, 6, 7, 8]
odd = 0
even = 0
if a[0] % 2 == 0:
    even += 1
else:
    odd += 1
if a[1] % 2 == 0:
    even += 1
else:
    odd += 1
if a[2] % 2 == 0:
    even += 1
else:
    odd += 1
if a[3] % 2 == 0:
    even += 1
else:
    odd += 1
if a[4] % 2 == 0:
    even += 1
else:
    odd += 1
if a[5] % 2 == 0:
    even += 1
else:
    odd += 1
if a[6] % 2 == 0:
    even += 1
else:
    odd += 1
if a[7] % 2 == 0:
    even += 1
else:
    odd += 1
print("The Odd numbers in the list are:", odd)
print("The Even numbers in the list are:", even)