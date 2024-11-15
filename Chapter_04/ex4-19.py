from vectors import scale, add

def linear_combination(scalars, *vectors):
    '''
    実数のリストと、その要素数と同じ数のベクトルを取り、単一のベクトルを返す。
    例えば、linear_combination([1,2,3],(1,0,0),(0,1,0),(0,0,1))は(1,2,3)を返す
    '''
    # ベクトルのスカラー倍と和を計算する関数をインポートする必要がある。
    # zip でまとめるのかな？
    output_vec = (0,0,0)
    for scalar, vector in zip(scalars, vectors):
        output_vec = add(scale(scalar, vector), output_vec)
    return output_vec

print(linear_combination([1,2,3],(1,0,0),(0,1,0),(0,0,1)))