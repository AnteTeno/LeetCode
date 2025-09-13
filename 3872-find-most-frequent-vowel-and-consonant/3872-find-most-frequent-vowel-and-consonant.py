class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}       # dict, not list
        consonants = {}   # dict, not list

        def isVowel(c):
            return c in "aeiou"   # fixed typo

        for c in s:
            if isVowel(c):
                count_v = s.count(c)
                vowels[c] = count_v
            else:
                count_c = s.count(c)
                consonants[c] = count_c

        # max frequency from each group
        max_v = max(vowels.values()) if vowels else 0
        max_c = max(consonants.values()) if consonants else 0

        return max_v + max_c
