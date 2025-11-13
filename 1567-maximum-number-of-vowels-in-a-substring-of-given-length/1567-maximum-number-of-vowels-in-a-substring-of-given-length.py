
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        slist = list(s)
        currentSum = sum(1 for ch in slist[:k] if ch in "aeiou")
        maxSum = currentSum
        n = len(s)

        for i in range(k, n):
            nextChar = 0
            leavingChar = 0
            if slist[i] in "aeiou":
                nextChar = 1
            if slist[i - k] in "aeiou":
                leavingChar = 1

            currentSum += nextChar - leavingChar
            maxSum = max(currentSum, maxSum)

        return maxSum