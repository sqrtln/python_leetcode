"""

283. 移动零
简单

提示
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]

提示:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


解法： 双指针，使用一个指针 j 来记录当前非零元素的最后一个位置，另一个指针 i 来遍历数组。当 nums[i] 不等于 0 时，将 nums[i] 赋值给 nums[j]，并将 j 加 1。最后将 j 之后的元素全部赋值为 0 即可。

"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

print(Solution().moveZeroes([0,1,0,3,12]))