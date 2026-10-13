class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l = [x ** 2 for x in nums]
        l.sort()
        n = len(nums)
        c, i, k = 0, 0, len(nums)
        while k != 0:
            c += l[n - i - 1]
            k -= 1
            if k != 0:
                c -= l[i]
                k -= 1
            i += 1
        return c