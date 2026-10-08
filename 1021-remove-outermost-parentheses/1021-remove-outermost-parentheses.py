class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = []
        c = 0
        for ch in s:
            if ch == '(':
                if c > 0:
                    l.append(ch)
                c += 1
            else:
                c -= 1
                if c > 0:
                    l.append(ch)
        return "".join(l)