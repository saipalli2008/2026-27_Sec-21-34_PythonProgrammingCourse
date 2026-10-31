# One row: three zeros on the same line
for i in range(1, 4):  # column_loop_var; range starts at 1, repeat 3 times
    print(0, end=" ")  # print one zero, stay on same line
print()  # move to next line after the row

# One column: three zeros, each on its own line
for i in range(1, 4):  # row_loop_var; range starts at 1, repeat 3 times
    print(0)  # print one zero and go to next line