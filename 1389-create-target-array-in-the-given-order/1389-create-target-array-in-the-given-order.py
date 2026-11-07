class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        l = []
        for i in range(len(nums)):
            l.insert(index[i], nums[i])
        return l