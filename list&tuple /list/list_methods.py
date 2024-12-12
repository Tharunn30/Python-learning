list = [2,1,3]
# list = ["banana", "apple", "litchi"]

#1. Append: list.append(4). It add one element at end
list.append(4)
print(list)  #[2,1,3,4]

#2. Extend: list.extend([4,5,6]). It add multiple elements at end
list.extend([4,5,6])
print(list)  #[2,1,3,4,5,6]

#3. Sort: list.sort(reverse=True). It sorts in descending order
list.sort() #For ascending order
list.sort(reverse=True) #For descending order
print(list)  #[1,2,3,4,5,6]

#4. Insert: list.insert(idx, el). Inserting element at index
list.insert(1, 5)
print(list)  #[1,5,2,3,4,5,6]

#5. Remove: list.remove(el). It removes the first occurrence of the element
list.remove(5)

#6. Pop: list.pop(idx). Removes a particular element
list.pop(1)
print(list)