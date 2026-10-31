rows = int(input("Enter grid size (rows and columns): "))
rows = 5  # start with 5; later use int(input(...))

for row in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for col in range(1, rows + 1):  # column_loop_var; range(1, rows + 1)
        if row == 1 or row == rows or col == 1 or col == rows:  # first/last row or first/last column?
            print("*", end=" ")  # print a star
        else:
            print(" ", end=" ")  # print a space
    print()  # next line after the row