class HashMixin:
    def __hash__(self):
        return sum(num for row in self.matrix for num in row) % 6


class Matrix(HashMixin):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Wrong shape!")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Wrong shape!")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] * other.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Wrong shape!")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = 0
                for k in range(self.cols):
                    value += self.matrix[i][k] * other.matrix[k][j]
                row.append(value)
            result.append(row)

        return Matrix(result)

