import numpy as np
from matrix_mixin import Matrix

np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

matrix_sum = matrix1 + matrix2
matrix_product = matrix1 * matrix2
matrix_multiply = matrix1 @ matrix2
path = "artifacts/2/"

matrix_sum.write_to_file(path + 'matrix+.txt')
matrix_product.write_to_file(path + 'matrix_mul.txt')
matrix_multiply.write_to_file(path + 'matrix@.txt')
