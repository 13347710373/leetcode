"""
914. 卡牌分组
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。

示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]

示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：

1 <= deck.length <= 10000
0 <= deck[i] < 10000
"""

def getzs(num):
    if num<2: return []
    a = 2
    res = []
    while a<=num:
        if num%a == 0:
            num = num/a
            res.append(a)
        else:
            a=a+1  
    return res

def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    dic = {}
    maxvalue = 0
    for d in deck:
        if d in dic:
            dic[d] +=1
        else:
            dic[d] = 1
        if dic[d]>maxvalue:maxvalue=dic[d]

    print(dic)

    lst = getzs(maxvalue)
    if (len(lst)<=0):return False

    di=[]
    for d in dic.values():
        if d not in di:
            di.append(d)
    
    print(di)

    for e in lst:
        flag = True
        for d in di:
            flag = flag & (d%e==0)
        if flag:return True

    return False

"""
执行用时 :28 ms, 在所有 Python 提交中击败了98.33%的用户
内存消耗 :13 MB, 在所有 Python 提交中击败了10.00%的用户
"""
deck = [1,1,2,2,2,3,3,3,3,3,3]
res = hasGroupsSizeX(deck)
print(res)