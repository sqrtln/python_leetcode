"""

977. 有序数组的平方

简单

给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。


示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
 
提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序

解法： 双指针，使用一个指针 slow 来记录当前非负数的第一个位置，另一个指针 fast 来遍历数组。当 nums[slow] < 0 时，slow 向右移动；当 nums[slow] >= 0 时，
fast 向右移动。比较 nums[slow] 和 nums[fast] 的绝对值，将较大的平方值放入结果数组中，并移动相应的指针。最后返回结果数组即可。    
"""
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        slow, fast = 0, len(nums) - 1
        result = [0] * len(nums)
        for i in range(len(nums) - 1, -1 , -1):
            if abs(nums[slow]) < abs(nums[fast]):
                result[i] = nums[fast] * nums[fast]
                fast -= 1
            else:
                result[i] = nums[slow] * nums[slow]
                slow += 1
        return result

        # new = []
        # for i in nums:
        #     new.append(i * i)
        # return sorted(new)

print(Solution().sortedSquares([-4,-1,0,3,10]))