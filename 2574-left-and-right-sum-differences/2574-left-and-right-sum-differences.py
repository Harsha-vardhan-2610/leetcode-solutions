class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = [0]
        r = [0]
        c = len(nums)
        for i in range(c - 1):
            l.append(nums[i] + l[i])
        for i in range(c - 1, 0, -1):
            r.insert(0, nums[i] + r[0])
        a = []
        for i in range(c):
            a.append(abs(l[i] - r[i]))
        return a