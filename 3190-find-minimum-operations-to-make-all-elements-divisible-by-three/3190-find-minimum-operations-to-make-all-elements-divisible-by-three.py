class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            d = nums[i] % 3
            c += min(d, 3 - d)
        return c