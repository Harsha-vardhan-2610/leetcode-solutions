from collections import Counter

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = Counter([0])
        for a in nums:
            _dp = deepcopy(dp)
            for k, v in _dp.items():
                dp[k | a] += v
        return dp[max(dp)]