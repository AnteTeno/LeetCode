class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(x):
            if (x == 'a' or x == 'e' or x == 'i' or 
                x == 'o' or x == 'u' or x == 'A' or 
                x == 'E' or x == 'I' or x == 'O' or 
                x == 'U'):
                return True
            else:
                return False
        
        vowels = []
        stringAsList = list(s)
        index_list = []
        for i, c in enumerate(s):
            if isVowel(c):
                index_list.append(i)
                vowels.append(c)
        reversed = vowels[::-1]

        for i, j in enumerate(index_list):
            print(i, j)
            stringAsList[j] = reversed[i]
        return "".join(stringAsList)

