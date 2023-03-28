# Напишите функцию для транспонирования матрицы


def transpose_matrix(matrix: list) -> list:
    #for row in matrix:
    #    print(row)
    #print('\n')
    matrix1 = zip(*matrix)
    for row in matrix1:
        print(row)


matr = [[1, 2, 3], [4, 5, 6], [3, 2, 1], [6, 5, 4]]
transpose_matrix(matr)
