matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def square_matrix_simple(matrix=[]):
    New_matrix = []

    if len(matrix) > 0:
        for element in matrix[:]:
            New_matrix.append(list(map(lambda x: x ** 2, element)))
    return New_matrix


new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
