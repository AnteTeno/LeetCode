class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        slist = list(s)
        currentSum = sum(1 for ch in slist[:k] if ch in "aeiou")
        maxSum = currentSum
        n = len(s)

        for i in range(k, n):
            nextChar = sum(1 for ch in slist[i] if ch in "aeiou")
            leavingChar = sum(1 for ch in slist[i - k] if ch in "aeiou")
            currentSum += nextChar - leavingChar
            maxSum = max(currentSum, maxSum)

        return maxSum