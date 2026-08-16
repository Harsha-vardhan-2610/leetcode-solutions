class Solution:
    def minPartitions(self, n: str) -> int:
        s = "9876543210"
        for x in s:
            if x in n:
                return int(x)