
import random
from transforms import matrix_multiply

def random_matrix(n):
    '''
    n×n次元のランダムな整数からなる行列を生成する。
    '''
    return tuple([tuple([random.randint(1, 10) for i in range(0, n)])
              for j in range(0, n)])

matrix1 = random_matrix(3)
matrix2 = random_matrix(3)
multiplied = matrix_multiply(matrix1, matrix2)

print(matrix1)
print(matrix2)
print(multiplied)

