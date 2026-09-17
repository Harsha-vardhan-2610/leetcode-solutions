class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l = 0
        for acc in accounts:
            l = max(l, sum(acc))
        return l