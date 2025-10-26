class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pairs = set()
        left = 0
        right = len(nums) - 1
        nums.sort()

        while left < right:
            if nums[left] + nums[right] == k and left not in pairs and right not in pairs:
                pairs.add(left)
                pairs.add(right)
                left += 1
                right -= 1
            elif (nums[left] + nums[right]) < k:
                left += 1
            else:
                right -= 1
        
        return len(pairs)/2

      
