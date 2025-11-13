class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        print(f"First sum: {currentSum}")
        maxSum = currentSum
        n = len(nums)
        for i in range(k, n):
            currentSum += nums[i] - nums[i - k]
            maxSum = max(currentSum, maxSum)

        return maxSum / k
