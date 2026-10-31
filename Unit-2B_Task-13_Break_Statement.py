n = int(input("Enter N (print until N, stop early at 5): "))
for i in range(1, n + 1):  # numbers from 1 to n (use range)
    if i == 5:  # stop when the number is 5
        print(f"Breaking for loop at number {i} (N was {n})")  # current number
        break
    print(f"for loop number = {i} (up to {n})")  # current number