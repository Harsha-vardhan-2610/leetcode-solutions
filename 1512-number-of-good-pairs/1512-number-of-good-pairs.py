from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        s = 0
        for i in c.keys():
            s += c[i] * (c[i] - 1) // 2
        return s