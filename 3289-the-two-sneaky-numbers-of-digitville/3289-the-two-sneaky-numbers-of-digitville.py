class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        l = []
        for i, j in c.items():
            if j > 1:
                l.append(i)
        return sorted(l)