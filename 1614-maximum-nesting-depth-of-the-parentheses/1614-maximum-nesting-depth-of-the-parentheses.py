class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        m = 0

        for ch in s:
            if ch == '(':
                c += 1
            elif ch == ')':
                m = max(m, c)
                c -= 1
        return m