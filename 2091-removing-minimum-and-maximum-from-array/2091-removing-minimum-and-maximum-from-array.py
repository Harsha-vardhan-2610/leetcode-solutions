class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minidx = nums.index(min(nums))
        maxidx = nums.index(max(nums))

        left = min(minidx, maxidx)
        right = max(minidx, maxidx)

        return min(n - left, right + 1, n - right + left + 1)