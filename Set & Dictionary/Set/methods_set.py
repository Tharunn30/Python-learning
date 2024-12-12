#set is mutable -> It can add and remove
#Elements of set is immutable -> You cant change the elements of set

collection = set()

#Method 1: .add = It adds to the set
collection.add(1)
collection.add(2)
collection.add(3)
# collection.add([1, 2, 3]) #Values that immutable can be added in set because they have a hash value. Value inside set are immutable (they cant be changed). Known as unhashable.
print(collection) # output: {1, 2, 3}

#Method 2: .remove = It removes from the set
collection.remove(2)
print(collection)  # Output: {1, 3}

#Method 3: .clear = Empties the set
collection.clear()

#Method 4: .pop = Pops a random value from set
collection1 = {"hello","hi","world","car"}
collection1.pop()

#Important methods
#Method 5: .union = Combines both values and returns new
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
 
#Method 6: .intersection = Combines common values and returns new
print(set1.intersection(set2))