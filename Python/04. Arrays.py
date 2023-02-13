

# Declare a new array

fruits = [] #empty array
moreData = ["Wilfred", 25, [], "random data", [1,2,3,4]] #array using different types of values

print(fruits)
#Result: []

print(moreData)
#Result: ["Wilfred", 25, [], "random data", [1,2,3,4]]

# Access to specific element in array

print(moreData[0])
#Result: Wilfred
print(moreData[4])
#Result: [1,2,3,4]
print(moreData[4][2])
#Result: 3

# Print each element within array (02. Loops.py)


# Update a specific element within the array

moreData[1] = 11
print(moreData)
#Result: ["Wilfred", 11, [], "random data", [1,2,3,4]]
moreData[4][0] = 999
print(moreData)
#Result: ["Wilfred", 11, [], "random data", [999,2,3,4]]
