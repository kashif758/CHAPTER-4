'''
Python lists are containers used to store a collection of values,
where each value can be of any data type.
'''

Friends = ["Apple", "Orange", 5 , 38.04, "Juha", "Miskat"]

print(Friends[0])     # Accessing the first element

'''
Strings cannot be changed because they are immutable data types, 
but you can create new strings using strings.
Lists, on the other hand, are mutable,
so you can directly change the elements in a list.
'''
Friends[0]= "Banana"  # Lest Are Mutable
print(Friends[0])    # Accessing the modified first element

'''
A list can be indexed just like a string,
meaning you can access any element in a list using its index position.
'''
print(Friends[0])
print(Friends[1])
print(Friends[2])
print(Friends[3])
print(Friends[4])
print(Friends[5])

print(Friends[2:5]) # index slicing
print(Friends[1:])  # from index 1 to end
