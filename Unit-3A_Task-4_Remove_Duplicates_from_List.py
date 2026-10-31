list_data = [1, 2, 2, 3, 1, 4, 3]  # e.g. [1, 2, 2, 3, 1, 4, 3]
unique = []  # empty list []

for item in list_data:  # each item in list_data
    if item not in unique:  # item not already in unique
        unique.append(item)  # append item

print("Original:", list_data)
print("Without duplicates:", unique)