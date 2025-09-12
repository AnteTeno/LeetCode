class Solution:
    def doesAliceWin(self, s: str) -> bool:
        def isVowel(x):
            if (x == 'a' or x == 'e' or x == 'i' or 
                x == 'o' or x == 'u' or x == 'A' or 
                x == 'E' or x == 'I' or x == 'O' or 
                x == 'U'):
                return True
            else:
                return False

        vowels = []

        for i in s:
            if isVowel(i):
                vowels.append(i)
        if not vowels:
            return False
        elif len(vowels) % 2 == 1:
            return True
        else:
            return True