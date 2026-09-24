class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            num = sum(map(int, str(num)))
            if num == i:
                return i
        return -1