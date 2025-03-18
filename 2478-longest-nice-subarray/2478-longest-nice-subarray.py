from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bitmask = 0
        left = 0
        max_len = 0

        for right in range(len(nums)):  
            while (bitmask & nums[right]) != 0:  
                bitmask ^= nums[left]
                left += 1

            bitmask |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len

nums = [1, 3, 8, 48, 10]
solution = Solution()
print(solution.longestNiceSubarray(nums))
