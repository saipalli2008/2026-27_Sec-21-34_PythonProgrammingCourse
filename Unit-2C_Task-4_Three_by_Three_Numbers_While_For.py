num = 1  # start counting from 1
row_loop_var = 1  # start row_loop_var at 1

while row_loop_var <= 3:  # keep going while row_loop_var is within 1..3
    for col in range(1, 4):  # column_loop_var; range(1, 4) — each column
        print(num, end=" ")  # print the current number
        num = num + 1  # increase num by 1 for the next cell
    print()  # move to next line after the row
    row_loop_var = row_loop_var + 1  # increase row_loop_var by 1