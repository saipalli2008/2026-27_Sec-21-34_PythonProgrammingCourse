rows = 3  # e.g. 3

for row_loop_var in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):  # column_loop_var_spaces; range(1, rows - row_loop_var + 1)
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):  # column_loop_var_dots; range(1, 2 * row_loop_var)
        print("*", end=" ")  # print one star
    print()