"""
https://leetcode.cn/problems/plus-one/description/

66. 加一
简单

给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组。


示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。
示例 3：

输入：digits = [9]
输出：[1,0]
解释：输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。

解法： 从后往前遍历，如果当前位小于9，则直接加1并返回结果；如果当前位等于9，则将当前位置为0，并继续向前遍历。最后，如果所有位都是9，则需要在数组开头添加一个1。

"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
        #     else:
        #         digits[i] = 0
        # return [1] + digits
        digits = [0] + digits
        digits[len(digits)-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
        return digits if digits[0] == 1 else digits[1:]

print(Solution().plusOne([1,9,9,5,9]))