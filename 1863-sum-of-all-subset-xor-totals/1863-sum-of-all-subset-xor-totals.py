class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            c |= num
        return c * (1 << (len(nums) - 1))