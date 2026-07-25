class Solution:
    def maxProduct(self, n: int) -> int:
        c, d = sorted(str(n))[-2:]
        return int(c) * int(d)