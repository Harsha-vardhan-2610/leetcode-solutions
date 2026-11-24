class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        c = 0

        for ch in s:
            if num % int(ch) == 0:
                c += 1
        
        return c