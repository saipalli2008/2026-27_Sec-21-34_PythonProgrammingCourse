n = int(input("Enter N (print 1 to N, skip even numbers): "))
for i in range(1, n + 1):  # numbers from 1 to n (use range)
    if i % 2 == 0:  # is the number even?
        print(f"Skipping even number {i} with continue (N is {n})")  # current number
        continue
    print(f"for loop odd number = {i} (up to {n})")  # current number