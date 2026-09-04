class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])
        
        prefix = nums[0]
        for i in range(n):
            if prefix - suffix[i] <= k:
                return i
            prefix = max(prefix, nums[i])
        
        return -1