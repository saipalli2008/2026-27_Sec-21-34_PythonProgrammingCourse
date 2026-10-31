num = 1  # start counting from 1

for i in range(1, 4):  # row_loop_var; range(1, 4) — each row
    for j in range(1, 4):  # column_loop_var; range(1, 4) — each column
        print(num, end=" ")  # print the current number
        num = num + 1  # increase num by 1 for the next cell
    print()  # move to next line after the row