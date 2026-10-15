class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        c, n = 0, len(nums)

        for i in range(n):
            for j in range(i, n):
                c += len(set(nums[i : j + 1])) ** 2
        
        return c