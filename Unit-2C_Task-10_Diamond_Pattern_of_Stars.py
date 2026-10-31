rows = int(input("Enter number of rows (half diamond): "))

# Upper half (including middle)
for row_loop_var in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):  # column_loop_var_spaces
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):  # column_loop_var_dots; range(1, 2 * row_loop_var)
        print("*", end=" ")
    print()

# Lower half
for row_loop_var in range(rows - 1, 0, -1):  # row_loop_var; range(rows - 1, 0, -1)
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):  # column_loop_var_spaces
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):  # column_loop_var_dots
        print("*", end=" ")
    print()