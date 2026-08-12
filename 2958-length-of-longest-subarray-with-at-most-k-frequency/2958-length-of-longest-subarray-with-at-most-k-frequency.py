class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, l = 0, 0
        freq = defaultdict(int)

        for i, x in enumerate(nums):
            freq[x] += 1
            while freq[x] > k:
                freq[nums[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        
        return ans