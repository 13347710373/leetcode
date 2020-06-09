"""
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
def maximalSquare(matrix):
    m = 0
    a = len(matrix)
    b = 0 if a==0 else len(matrix[0])
    for i in range(0,a):
        for j in range(0,b):
            matrix[i][j] = int(matrix[i][j])
            if (matrix[i][j] != 0):
                n = min(
                0 if (i*j==0) else matrix[i-1][j-1],
                0 if i==0 else matrix[i-1][j],
                0 if j==0 else matrix[i][j-1])+1
                if n>m:m=n
                matrix[i][j] = n
    return m*m

m= [["1"]]
maximalSquare(m)
