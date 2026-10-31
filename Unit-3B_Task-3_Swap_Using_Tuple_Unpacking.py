first_number = 10  # e.g. 10
second_number = 20  # e.g. 20

print("Before:", first_number, second_number)

first_number, second_number = second_number, first_number  # swap with unpacking

print("After:", first_number, second_number)