class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        for i in range(1, n + 1):
            c += nums[i - 1] ** 2 if n % i == 0 else 0
        return c