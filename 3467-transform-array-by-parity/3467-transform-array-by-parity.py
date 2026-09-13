class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                l.append(0)
            else:
                l.append(1)
        return sorted(l)