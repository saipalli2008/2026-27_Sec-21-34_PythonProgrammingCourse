rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to print (e.g. * or 0): ")
rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to print (e.g. * or 0): ")

for row_loop_var in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for column_loop_var in range(1, row_loop_var + 1):  # column_loop_var; range(1, row_loop_var + 1)
        print(symbol, end=" ")  # print the symbol variable
    print()  # next line after the row