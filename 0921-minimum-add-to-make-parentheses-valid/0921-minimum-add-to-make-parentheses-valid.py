class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = 0
        res = 0
        for ch in s:
            if ch == '(':
                c += 1
            else :
                c -= 1
            
            if c < 0:
                res += 1
                c = 0

        if c > 0:
            res += c
        return abs(res)