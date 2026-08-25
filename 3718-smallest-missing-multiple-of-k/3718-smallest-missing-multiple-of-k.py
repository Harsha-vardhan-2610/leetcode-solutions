class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = set(nums)
        i = 1
        while True:
            if i * k not in n:
                return i * k
            i += 1