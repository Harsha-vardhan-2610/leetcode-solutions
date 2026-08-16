class Solution:
    def minPartitions(self, n: str) -> int:
        c = 0
        for i in n:
            c = max(c, int(i))
        return c