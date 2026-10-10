class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] < target:
                    c += 1
        return c