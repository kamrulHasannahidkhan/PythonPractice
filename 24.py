def transpose_matrix(matrix: list) -> list:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Example Usage
m = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(m))  # Output: [[1, 4], [2, 5], [3, 6]]