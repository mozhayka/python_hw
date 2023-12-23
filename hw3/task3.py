import numpy as np

from matrix import Matrix

A = Matrix([
    [1, 0],
    [0, 2]]
)

C = Matrix([
    [3, 0],
    [0, 0]
])

B = Matrix([
    [1, 1],
    [1, 0]
])

D = B

assert (hash(A) == hash(C)) and (A.matrix != C.matrix) and (B.matrix == D.matrix) and ((A @ B).matrix != (C @ D).matrix)

path = "artifacts/3/"
np.savetxt(path + 'A.txt', A.matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'B.txt', B.matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'C.txt', C.matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'D.txt', D.matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'AB.txt', (A @ B).matrix, delimiter='\t', fmt='%d')
np.savetxt(path + 'CD.txt', (C @ D).matrix, delimiter='\t', fmt='%d')

with open(path + "hash.txt", "w") as f:
    f.write(f"AB hash: {hash(A @ B)}\n")
    f.write(f"CD hash: {hash(C @ D)}")
