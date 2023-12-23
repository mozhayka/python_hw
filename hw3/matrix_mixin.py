import numpy as np


class OperationsMixin:
    def __add__(self, other):
        return self.__class__(np.add(self.matrix, other.matrix))

    def __mul__(self, other):
        return self.__class__(np.multiply(self.matrix, other.matrix))

    def __matmul__(self, other):
        return self.__class__(np.matmul(self.matrix, other.matrix))


class FilePrintMixin:
    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


class StrMixin:
    def __str__(self):
        return "\n".join("\t".join(map(str, row)) for row in self.matrix)


class GetSetMixin:
    @property
    def data(self):
        return self.matrix

    @data.setter
    def data(self, value):
        self.matrix = value


class Matrix(OperationsMixin, FilePrintMixin, StrMixin, GetSetMixin):
    def __init__(self, matrix):
        self.matrix = matrix
