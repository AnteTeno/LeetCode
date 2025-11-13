class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        maxLength = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            maxLength = max(i - left + 1, maxLength)
        return maxLength