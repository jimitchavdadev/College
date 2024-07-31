def demonstrate_list_operations():
    # 1. Creating Lists
    list1 = [1, 2, 3, 4, 5]
    list2 = ['apple', 'banana', 'cherry']
    list3 = [1.1, 2.2, 3.3]
    list4 = [1, 'apple', 3.5, [2, 3]]
    print("List1:", list1)
    print("List2:", list2)
    print("List3:", list3)
    print("List4:", list4)

    # 2. Indexing
    print("First element of list1:", list1[0])
    print("Second element of list2:", list2[1])
    print("Last element of list3:", list3[-1])
    print("Element at index 2 of list4:", list4[2])
    print("Nested list element of list4:", list4[3][1])

    # 3. Slicing
    print("First three elements of list1:", list1[:3])
    print("Elements from index 1 to 4 of list1:", list1[1:4])
    print("All elements of list1 from index 2:", list1[2:])
    print("Elements from the end to index 2 of list1:", list1[-3:])
    print("Reversed list1:", list1[::-1])

    # 4. Appending and Extending
    list1.append(6)
    print("After appending 6:", list1)
    list1.extend([7, 8])
    print("After extending with [7, 8]:", list1)

    # 5. Inserting Elements
    list1.insert(2, 'inserted')
    print("After inserting 'inserted' at index 2:", list1)

    # 6. Removing Elements
    list1.remove('inserted')
    print("After removing 'inserted':", list1)
    removed_element = list1.pop(3)
    print("After popping element at index 3:", list1)
    print("Popped element:", removed_element)
    list1.clear()
    print("After clearing all elements:", list1)

    # 7. List Comprehensions
    squares = [x**2 for x in range(10)]
    print("Squares of numbers from 0 to 9:", squares)
    evens = [x for x in range(10) if x % 2 == 0]
    print("Even numbers from 0 to 9:", evens)

    # 8. Finding Elements
    list1 = [1, 2, 3, 4, 4]
    print("Index of 4 in list1:", list1.index(4) if 4 in list1 else "Not found")
    print("Count of 2 in list1:", list1.count(2))

    # 9. Sorting and Reversing
    list5 = [3, 1, 4, 1, 5, 9]
    list5.sort()
    print("Sorted list5:", list5)
    list5.reverse()
    print("Reversed list5:", list5)

    # 10. Copying Lists
    list6 = list5.copy()
    print("Shallow copy of list5:", list6)
    list7 = list5[:]
    print("Sliced copy of list5:", list7)

    # 11. Nested Lists
    nested_list = [[1, 2], [3, 4], [5, 6]]
    print("Nested list:", nested_list)
    print("Accessing element [1][0]:", nested_list[1][0])

    # 12. List Operations
    list8 = [1, 2, 3]
    list9 = [4, 5, 6]
    concat_list = list8 + list9
    print("Concatenated list:", concat_list)
    repeat_list = list8 * 3
    print("Repeated list8:", repeat_list)

if __name__ == "__main__":
    demonstrate_list_operations()
