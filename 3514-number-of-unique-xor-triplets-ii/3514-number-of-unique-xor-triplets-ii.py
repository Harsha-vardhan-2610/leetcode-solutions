class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            for y in nums:
                s.add(x ^ y)
        
        ans = set()
        for x in nums:
            for y in s:
                ans.add(x ^ y)
        
        return len(ans)