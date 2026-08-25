class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = set(nums)
        i = 1
        while True:
            if i % k == 0:
                if i not in n:
                    return i
            i += 1