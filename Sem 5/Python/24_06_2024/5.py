# Lists
list1 = [1, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'cherry']
list3 = [1.1, 2.2, 3.3]
list4 = [1, 'apple', 3.5, [2, 3]]
print("List1:", list1)
print("List2:", list2)
print("List3:", list3)
print("List4:", list4)

# Indexing
print("Second element of list2:", list2[1])
print("Last element of list3:", list3[-1])
print("Nested list element of list4:", list4[3][1])

# Slicing
print("First three elements of list1:", list1[:3])
print("Elements from index 1 to 4 of list1:", list1[1:4])
print("Elements from the end to index 2 of list1:", list1[-3:])
print("Reversed list1:", list1[::-1])

# Removing Elements
list1.clear()
print("After clearing all elements:", list1)

# List Comprehensions
squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9:", squares)

# Sorting
list5 = [3, 1, 4, 1, 5, 9]
list5.sort()
print("Sorted list5:", list5)

list8 = [1, 2, 3]
list9 = [4, 5, 6]
concat_list = list8 + list9
print("Concatenated list:", concat_list)
