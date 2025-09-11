class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        length = len(flowerbed)
        if length == 1 and n > 1 :
            return False
        elif length == 1 and n == 0:
            return True
        elif length == 1 and n == 1 and flowerbed[0] == 0:
            return True

        for i, j in enumerate(flowerbed):
            if i == 0:
                if j == 0 and flowerbed[i + 1] != 1:
                    counter += 1
                    flowerbed[i] = 1
            elif i == length - 1:
                if j == 0 and flowerbed[i - 1] != 1:
                    counter += 1
                    flowerbed[i] = 1
            elif j == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                counter += 1
                flowerbed[i] = 1
        if counter >= n:
            return True
        return False