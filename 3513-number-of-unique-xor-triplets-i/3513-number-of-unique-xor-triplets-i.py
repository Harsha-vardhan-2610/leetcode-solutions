class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        return 2 ** len(bin(max(nums))[2:]) if n > 2 else n