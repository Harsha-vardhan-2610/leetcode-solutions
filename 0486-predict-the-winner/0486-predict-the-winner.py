class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if ~n & 1: return True

        @cache
        def diff(i, j):
            if i == j: return nums[i]
            return max(nums[i] - diff(i + 1, j), nums[j] - diff(i, j - 1))
        
        return diff(0, n - 1) >= 0