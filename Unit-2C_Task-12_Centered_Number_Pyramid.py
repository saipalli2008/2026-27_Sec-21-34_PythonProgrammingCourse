rows = 5  # e.g. 5

for row_loop_var in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):  # column_loop_var_spaces; range(1, rows - row_loop_var + 1)
        print(" ", end=" ")
    for column_loop_var in range(1, 2 * row_loop_var):  # column_loop_var; range(1, 2 * row_loop_var)
        print(column_loop_var, end=" ")  # print 1, 2, 3, ... with a space between
    print()