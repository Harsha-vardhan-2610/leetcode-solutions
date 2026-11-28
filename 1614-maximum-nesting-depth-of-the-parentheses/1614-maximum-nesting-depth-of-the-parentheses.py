class Solution:
    def maxDepth(self, s: str) -> int:
        c, m = 0, 0
        for ch in s:
            if ch == '(':
                c += 1
            elif ch == ')':
                m = max(m, c)
                c -= 1
        return m