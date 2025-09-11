class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = []
        vowels_indexes = []
        def isVowel(x):
            if (x == 'a' or x == 'e' or x == 'i' or 
                x == 'o' or x == 'u' or x == 'A' or 
                x == 'E' or x == 'I' or x == 'O' or 
                x == 'U'):
                return True
            else:
                return False

            
        for i, c in enumerate(s):
            if isVowel(c):
                vowels.append(c)
                vowels_indexes.append(i)
                
        vowels_indexes.sort()
        vowels.sort()
        
        s_list = list(s)

        for i, j in enumerate(vowels_indexes):
            s_list[j] = vowels[i] 
        
        return "".join(s_list)
        

                