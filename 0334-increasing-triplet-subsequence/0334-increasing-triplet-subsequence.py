class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        middle = float('inf')

        for i in nums:
            if i <= smallest:
                smallest = i
            elif i <= middle:
                middle = i
            else:
                return True
        return False
