class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_num = max(candies)
        for num in range(len(candies)):
            if candies[num] + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result