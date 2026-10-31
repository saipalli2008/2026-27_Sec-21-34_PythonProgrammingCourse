list_data = [3, 1, 4, 1, 5]  # e.g. [3, 1, 4, 1, 5]
print("Original:", list_data)

list_data.append(9)  # append 9 at the end
print("After append:", list_data)

list_data.insert(0, 7)  # insert 7 at index 0
print("After insert:", list_data)

list_data.remove(1)  # remove first matching 1
print("After remove:", list_data)

list_data.sort()  # sort ascending
print("After sort:", list_data)

list_data.reverse()  # reverse the list
print("After reverse:", list_data)