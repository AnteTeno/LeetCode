class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n, m = len(str1), len(str2)

        def isDivisor(l):
            if n % l or m % l:
                return False
            f1, f2 = n // l, m // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(n, m), 0, -1):  #iterate from minimum of len1 and len2 to 0, by incrementing with -1
            if isDivisor(l):
                return str1[:l]
        return ""
