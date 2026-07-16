class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        narr = []
        m = nums[0]
        for i in range(n):
            m = max(m, nums[i])
            narr.append(gcd(nums[i], m))
        
        narr.sort()
        c = 0
        l, r = 0, n - 1

        while l < r:
            c += gcd(narr[l], narr[r])
            l += 1
            r -= 1
        
        return c
