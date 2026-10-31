rows = 3  # e.g. 3

# Upper half
for row_loop_var in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):  # leading spaces
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):  # column_loop_var_dots; range(1, 2 * row_loop_var)
        if column_loop_var_dots == 1 or column_loop_var_dots == 2 * row_loop_var - 1:  # first or last position in this row?
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half (same idea with row_loop_var from rows-1 down to 1)
for row_loop_var in range(rows - 1, 0, -1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end=" ")
    for column_loop_var_dots in range(1, 2 * row_loop_var):
        if column_loop_var_dots == 1 or column_loop_var_dots == 2 * row_loop_var - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()