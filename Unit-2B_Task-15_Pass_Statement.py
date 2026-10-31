n = int(input("Enter N (use pass for multiples of 3): "))
for i in range(1, n + 1):  # numbers from 1 to n (use range)
    if i % 3 == 0:  # is it a multiple of 3?
        pass  # do nothing here yet
        print(f"Used pass for multiple of 3: {i} (N is {n})")  # current number
    else:
        print(f"for loop number = {i} (up to {n})")  # current number