class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = 65535
        i = 0
        sums = 0
        sublength = 0
        for j in range(len(nums)):
            sums += nums[j]
            while sums >= target:
                sublength = (j - i + 1)
                result = result if result < sublength else sublength
                sums -= nums[i]
                i += 1

        return 0 if result == 65535 else result
    
print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))