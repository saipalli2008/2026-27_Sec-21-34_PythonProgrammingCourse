matrix_a = [[1, 2], [3, 4]]  # e.g. [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]  # e.g. [[5, 6], [7, 8]]

rows = len(matrix_a)  # len(matrix_a)
cols = len(matrix_a[0])  # len(matrix_a[0])

result = []
for i in range(rows):  # i in range(rows)
    row = []
    for j in range(cols):  # j in range(cols)
        row.append(matrix_a[i][j] + matrix_b[i][j])  # matrix_a[i][j] + matrix_b[i][j]
    result.append(row)

print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("Sum:", result)