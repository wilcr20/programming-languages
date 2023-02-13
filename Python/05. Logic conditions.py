
# *************** If, elif and else statements ***************
print("Using If/else statements ...\n")

n = 5
if n + 3 == 8:
    print(True)
else:
    print(False)
#Result: True

if n - 2 == 0:
    print(True)
else:
    print(False)
#Result: false


if n == 2:
    print(2)
elif n == 3:
    print(3)
elif n == 5:
    print(5)
else:
    print(0) # Last option
#Result: 5



# *************** AND condition ***************
print("\nUsing AND condition ...\n")

n = 10
if n>0 and n<15:
    print(True)
else:
    print(False)
#Result: True


if (n>0 and n<15) and len("Python") == 1:
    print(True)
else:
    print(False)
#Result: False



# *************** OR condition ***************
print("\nUsing OR condition ...\n")

array = [1, 2, 3, "ABC"]

if len(array) == 0 or 3+3 == 6:
    print(True)
else:
    print(False)
        

if array[0] == 2 or len(array) == 14:
    print(True)
else:
    print(False)    





