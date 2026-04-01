"""
34. 在排序数组中查找元素的第一个和最后一个位置

中等

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]

"""
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        left = 0 
        right = len(nums)-1
        while left < right:
            middle = left + (right - left)//2
            if(nums[middle] >= target):
                right = middle      
            else:
                left = middle + 1  
        left2, right2 = left, len(nums) - 1
        if not nums[left] == target:
            return [-1, -1]
        while left2 < right2:
            middle2 = left2 + (right2 - left2) // 2
            if nums[middle2] <= target:
                left2 = middle2 + 1
            else:
                right2 = middle2
        return [left, left2] if nums[left2] == target else [left, left2 -1]

print(Solution().searchRange([5,7,7,8,8,10], 8))