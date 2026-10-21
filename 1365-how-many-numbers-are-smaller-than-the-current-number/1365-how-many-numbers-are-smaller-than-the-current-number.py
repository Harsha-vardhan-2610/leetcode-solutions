class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
        return [d[x] for x in nums]