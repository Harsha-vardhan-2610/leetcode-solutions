class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        l = []
        for i in range(0, len(nums), 2):
            c = [nums[i + 1]]
            l += nums[i] * c
        return l