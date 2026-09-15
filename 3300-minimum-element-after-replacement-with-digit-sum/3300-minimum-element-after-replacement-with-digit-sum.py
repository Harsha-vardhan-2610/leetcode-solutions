class Solution:
    def minElement(self, nums: List[int]) -> int:
        def integer(n):
            c = 0
            while n > 0:
                c += n % 10
                n //= 10
            return c
        l = []
        for i in range(len(nums)):
            l.append(integer(nums[i]))
        return min(l)