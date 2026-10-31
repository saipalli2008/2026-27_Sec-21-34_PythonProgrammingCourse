total_input_numbers = int(input("Enter how many numbers: "))
largest = float(input("Enter a number: "))  # start with the first number

for _ in range(total_input_numbers - 1):  # remaining numbers only (total_input_numbers - 1 times)
    next_number = float(input("Enter a number: "))  # read the next number
    if next_number > largest:  # is this number greater than largest?
        largest = next_number  # update largest

print(f"Largest among {total_input_numbers} numbers is {largest}")