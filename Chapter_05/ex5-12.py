from transforms import matrix_multiply

def matrix_power(power, matrix):
    '''
    行列を指定された整数だけ累乗する。
    '''
    result = matrix_multiply(matrix, matrix)
    for i in range(0, power-1):
        result = matrix_multiply(result, matrix)

    return result