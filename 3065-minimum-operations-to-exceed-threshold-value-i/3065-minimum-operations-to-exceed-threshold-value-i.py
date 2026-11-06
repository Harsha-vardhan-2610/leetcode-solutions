class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l = len(nums)
        c = l
        for i in range(l):
            if nums[i] >=  k:
                c -= 1
        return c