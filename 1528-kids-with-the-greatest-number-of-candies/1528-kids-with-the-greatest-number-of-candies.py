class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        pointer = 0
        answer = []
        maxCandy = max(candies)
        while pointer < len(candies):
            if(candies[pointer] + extraCandies >= maxCandy):
                answer.append(True)
            else:
                answer.append(False)
            pointer += 1
        return answer