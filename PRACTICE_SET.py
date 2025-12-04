'''
1. Write a program to store seven fruits in a list entered by the user.
2. write a program to accept marks of 6 student and display them in a sorted manner.
3. Check the a type cannot be changed in python.
4. write a program to sum a list with 4 numbers.
5. write a program to count the number of zeros in the following tuple.[a = (7, 0, 8, 0, 3, 0, 5)]

'''

# 1. Store seven fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruits.append(input("Enter the name of fruit {}: ".format(i+1))) # Append the entered fruit to the list
print("Fruits entered:", fruits)

# 2. Accept marks of 6 students and display them in a sorted manner.
marks = []
for i in range(6):
    marks.append(int(input("Enter marks of student {}: ".format(i+1)))) # Append the entered marks to the list
marks.sort() # Sort the marks
print("Sorted marks:", marks)

# 3. Check that a type cannot be changed in Python.
a = 10
print("Original type of a:", type(a)) # Print original type
a = "Hello"
print("New type of a after changing value:", type(a)) # Print new type
# Note: In Python, variables are dynamically typed, so the type can change.

# 4. Sum a list with 4 numbers.
numbers = []
for i in range(4):
    numbers.append(int(input("Enter number {}: ".format(i+1)))) # Append the entered number to the list
total_sum = sum(numbers) # Calculate the sum of the list
print("Sum of the numbers:", total_sum)

# 5. Count the number of zeros in the following tuple.
a = (7, 0, 8, 0, 3, 0)
zero_count = a.count(0) # Count the number of zeros in the tuple
print("Number of zeros in the tuple:", zero_count)
