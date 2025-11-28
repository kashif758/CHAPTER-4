a = ["Apple", "Orange", 5 , 38.04, "Juha", "Miskat"]

print(a)

a.append("Banana")  # Adding an element to the end of the list
print(a)


'''
append() → শেষে যোগ
insert() → index-এ যোগ
remove() → মান মুছে
pop() → index-এর মান মুছে return
clear() → সব মুছে
sort() → সাজায়
reverse() → উল্টো
count() → কয়বার আছে
index() → কোন index-এ
extend() → দুই list জোড়া
copy() → list-এর কপি
'''
x  = [1, 2, 3]
x.append(4)# Appending an element to the list
print(x)
x.insert(1, 0) # Inserting an element at index 1
print(x)
x.remove(3) # Removing the element with value 3
print(x)
x.sort() # Sorting the list in ascending order
print(x)
x.pop(0) # Removing and returning the last element
print(x)
x.insert(0, 5) # Insert 5 such that its index in the list is 0
print(x)