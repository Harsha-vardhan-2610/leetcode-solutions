class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l = 0, 0
        c = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r += 1
            if s[i] == 'L':
                l += 1
            
            if r == l:
                c += 1
                r, l = 0, 0
        
        return c