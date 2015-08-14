from __future__ import division
import numpy
print '----------------------------------'
A = numpy.array([[1, 2, 3], [4, 5, 6]])
print(A.transpose())
print '----------------------------------'
A = numpy.array([[1, 2], [3, 4]])
print(numpy.linalg.inv(A))
print '----------------------------------'

A = numpy.array([[1, 2, 3], [1, 2, 1]])
B = numpy.array([[2, 1, 3], [-1, 0, 5]])
# C = numpy.dot(A, B) # Error!
B = B.transpose()
C = numpy.dot(A, B)
print(C)

print '----------------------------------'


def main():
    A = get_matrix()
    print(matrix_tutorial(A))

def get_matrix():
    mat = []
    [n, m] = [int(x) for x in raw_input().strip().split(" ")]
    for i in range(n):
        row = [int(x) for x in raw_input().strip().split(" ")]
        mat.append(row)
    return numpy.array(mat)

def matrix_tutorial(A):
    # 2
    B = A.transpose()
    # 3
    try:
        C = numpy.linalg.inv(A)
    except numpy.linalg.linalg.LinAlgError:
        return 'not invertibles'
    # 4
#     return numpy.sum([1 for x in C.flat if x>0])
    return numpy.sum(C>0)
if __name__ == "__main__":
    main()

