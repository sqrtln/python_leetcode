"""
https://leetcode.cn/problems/valid-perfect-square/description/
367. 有效的完全平方数
简单

给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
不能使用任何内置的库函数，如  sqrt 。


示例 1：

输入：num = 16
输出：true
解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
示例 2：

输入：num = 14
输出：false
解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。

解法： 二分查找，判断 mid*mid 和 num 的关系，如果 mid*mid < num，则 left = mid + 1；如果 mid*mid > num，则 right = mid - 1；如果 mid*mid == num，则返回 true。最后，如果 left > right，则返回 false。

"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        right = num
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return left * left == num
    
print(Solution().isPerfectSquare(16))
