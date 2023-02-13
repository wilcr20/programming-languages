
# print(N ,end=" ") will write the variable N in the same line (just for testing)
#len(N) will return how many elemanet has the variable N (N = string/array) 

# **************** For ****************
print("Using Loop For ...\n")

for n in range (0,5):
    print(n, end=" ")
print()
# Result: 0 1 2 3 4


for n in range (5,0, -1):
    print(n, end=" ")
print()
# Result: 5 4 3 2 1


for letter in "Python":
    print(letter, end=" ")
print()
# Result: P y t h o n


fruits = ["banana", "pears", "oranges"]
for fruit in fruits:
    print(fruit, end=" ")
print()
# Result: banana pears oranges


# **************** While ****************
print("\n\nUsing Loop While ...\n")

index = 0
while index < 5:
    print(index, end=" ")
    index = index + 1
print()
# Result: 0 1 2 3 4


index = 5
while index > 0:
    print(index, end=" ")
    index = index - 1
print()
# Result: 5 4 3 2 1


index = 0
while index < len("Python"):
    print("Python"[index], end = " ")
    index = index + 1
print()
# Result: P y t h o n


fruits = ["banana", "pears", "oranges"]
index = 0
while index < len(fruits):
    print(fruits[index], end = " ")
    index = index + 1
print()
# Result: banana pears oranges











