import numpy as np
from matrix import Matrix

np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

matrix_sum = matrix1 + matrix2
matrix_product = matrix1 * matrix2
matrix_multiply = matrix1 @ matrix2
path = "artifacts/1/"

# np.savetxt(path + 'matrix1.txt', matrix1.matrix, delimiter='\t', fmt='%d')
# np.savetxt(path + 'matrix2.txt', matrix2.matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'matrix+.txt', matrix_sum.matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'matrix_mul.txt', matrix_product.matrix, delimiter='\t', fmt='%d')  # Invalid file name: 'matrix*.txt'
np.savetxt(path + 'matrix@.txt', matrix_multiply.matrix, delimiter='\t', fmt='%d')
