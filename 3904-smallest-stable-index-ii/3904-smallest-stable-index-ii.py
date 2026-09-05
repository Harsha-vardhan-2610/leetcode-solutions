class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix = [0] * n
        prefix = [0] * n

        suffix[0] = nums[0]
        for i in range(1, n):
            suffix[i] = max(suffix[i - 1], nums[i])
        
        prefix[-1]  = nums[-1]
        for i in range(n - 2, -1, -1):
            prefix[i] = min(prefix[i + 1], nums[i])
        
        for i in range(n):
            if suffix[i] - prefix[i] <= k:
                return i
        else:
            return -1