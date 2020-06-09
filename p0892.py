"""
892. 三维形体的表面积

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：
输入：[[2]]
输出：10

示例 2：
输入：[[1,2],[3,4]]
输出：34

示例 3：
输入：[[1,0],[0,2]]
输出：16

示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32

示例 5：
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46

示例 6：
输入：[[2,3,4],[5,6,7],[8,9,1]]
输出：?

提示：
1 <= N <= 50
0 <= grid[i][j] <= 50
"""

def surfaceArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    num=0
    for j,lst in enumerate(grid):
        for i,l in enumerate(lst):
            num+=(l*6)
            num -= 2*(l-1) if l>0 else 0
            if i>0:num-= 2*lst[i] if lst[i]<lst[i-1] else 2*lst[i-1]

        if j>0:
            for k in range(0,len(grid[j])):
                num-= 2*grid[j][k] if grid[j][k]<grid[j-1][k] else 2*grid[j-1][k]

    return num

"""
2020-02-35 07:00:39
执行用时 :68 ms, 在所有 Python 提交中击败了96.88%的用户
内存消耗 :12.7 MB, 在所有 Python 提交中击败了9.09%的用户
"""
t =[[2,2,2],[2,1,2],[2,2,2]]
s = surfaceArea(t)
print(s)