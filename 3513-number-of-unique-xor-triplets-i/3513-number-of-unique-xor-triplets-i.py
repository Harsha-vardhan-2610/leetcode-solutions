class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return 2 ** len(bin(max(nums))[2:]) if len(nums) > 2 else len(nums)