"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
def longestPalindrome(s):
    m=0 
    res=""
    l = len(s)
    for i in range(0,l):
        a = 0
        arr = s[i]
        while(True):
            a=a+1
            if i-a<0:break
            if i+a>=l:break
            if s[i-a]!=s[i+a]:break
            arr = s[i-a]+arr + s[i+a]
        if len(arr)>m:
            m=len(arr)
            res=arr
    for i in range(0,l):
        if (i+1>=l):continue
        a = 0
        if (s[i]!=s[i+1]):
            continue
        arr = s[i]+s[i+1]
        while(True):
            a=a+1
            if i-a<0:break
            if i+a+1>=l:break
            if s[i-a]!=s[i+a+1]:break
            arr = s[i-a]+ arr + s[i+a+1]
        if len(arr)>m:
            m=len(arr)
            res=arr
    return res


longestPalindrome("sfsffjiewrrteedfsssfdgdfof")