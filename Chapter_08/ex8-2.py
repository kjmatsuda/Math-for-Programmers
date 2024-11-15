# 以下は自分の解答(間違い)
# def secant_line(f, x1, x2):
#     '''
#     関数f(x)と2つの値x1, x2 を取り、x1とx2が成す割線を表す関数を返す。
#     例えば、line = secant_line(f,x1,x2)と実行すると、line(3)はその割線のx = 3におけるy値を返す。
#     '''
#     def new_function(x):
#         dx = x2 - x1
#         dy = f(x2) - f(x1)
#         return dx / dy

#     return new_function

# def quadratic_function(x):
#     return x ^ 2 + 3

# line = secant_line(quadratic_function, x1, x2)
# line(3)

# 以下は本に記載の答え
def secant_line(f, x1, x2):
    def line(x):
        return f(x1) + (x-x1) * (f(x2)-f(x1))/(x2-x1)
    return line
