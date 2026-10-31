rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for space in range(1, rows - row + 1):  # column_loop_var_spaces; range(1, rows - row_loop_var + 1)
        print(" ", end="")  # single leading space for centering
    value = 1  # first value in a Pascal row is 1
    for col in range(1, row + 1):  # column_loop_var; range(1, row_loop_var + 1)
        print(value, end=" ")  # print current Pascal value
        value = value * (row - col) // col  # update using the formula
    print()