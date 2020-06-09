"""
45. 跳跃游戏 II

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
"""
def jump(nums):

    def getx(num):
        res=[]
        l = len(num)
        for i in range(0,l):
            res.append(num[i]-l+i)
        return res.index(max(res))

    t=0
    l = len(nums)
    i=0
    while(True):
        if i>l:break
        if l==1:break
        num = nums[i+1:i+1+nums[i]]
        if (nums[i]>=len(nums)-1-i):
            t=t+1
            break
        a = getx(num)
        t=t+1
        i=i+a+1

    return t

r = jump([2,3,1])
print(r)