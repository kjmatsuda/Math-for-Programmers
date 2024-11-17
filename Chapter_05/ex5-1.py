from transforms import rotate_z_by
from math import pi

def my_infer_matrix(n, transformation):
    '''
    第1引数は次元数、第2引数は関数(線形であると仮定したベクトル変換)を取る関数。
    この関数はn×nの正方行列(n個のタプルからなるn個のタプル)を返す。
    '''
    # つまりは標準基底ベクトルに第2引数の関数を適用した結果を返せばいいのかな？
    # 第1引数が次元数だから難しいなあ...
    # とりあえず、3次元と仮定して書いてみるか
    e1 = (1,0,0)
    e2 = (0,1,0)
    e3 = (0,0,1)
    T_e1 = transformation(e1)
    T_e2 = transformation(e2)
    T_e3 = transformation(e3)

    # 正しくはここで tuple(zip(T_e1, T_e2, T_e3))とする必要があった
    return (T_e1, T_e2, T_e3)

# 本に記載の答えは以下
def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i==j else 0 for j in range(1, n+1))
    standard_basis = [standard_basis_vector(i) for i in range(1, n+1)]
    cols = [transformation(v) for v in standard_basis]
    return tuple(zip(*cols))

print(my_infer_matrix(3, rotate_z_by(pi/2)))

print(infer_matrix(3, rotate_z_by(pi/2)))
