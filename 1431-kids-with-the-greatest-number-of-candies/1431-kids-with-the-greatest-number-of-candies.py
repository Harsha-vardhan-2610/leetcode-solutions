class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        m = max(candies)
        for c in candies:
            l.append(c + extraCandies >= m)
        return l