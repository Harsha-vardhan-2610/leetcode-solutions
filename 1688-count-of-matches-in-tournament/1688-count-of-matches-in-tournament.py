class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        x = n
        while x != 0:
            m += x // 2 + x % 2
            x = x // 2
        return m - 1