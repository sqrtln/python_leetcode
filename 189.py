"""
https://leetcode.cn/problems/rotate-array/
189. 轮转数组

中等

提示
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

解法： 反转数组的前 n-k 个元素，反转数组的后 k 个元素，最后反转整个数组。

"""
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k %= len(nums)

        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


print(Solution().rotate([1,2,3,4,5,6,7], 3)) 