class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(str(x))
        print(str(x)[::-1])
        return str(x)==str(x)[::-1]

print(Solution().isPalindrome(121))
