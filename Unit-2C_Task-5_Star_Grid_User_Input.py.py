rows = int(input("Enter grid size (rows and columns): "))
rows = 5  # start with 5; later use int(input(...))

for row in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for col in range(1, rows + 1):  # column_loop_var; range(1, rows + 1)
        print("*", end=" ")  # print one star
    print()  # next line after the row