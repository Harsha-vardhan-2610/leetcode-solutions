class Solution:
    def canAliceWin(self, n: int) -> bool:
        x = 10
        a = 0
        while True:
            if n >= x:
                a ^= 1
                n -= x
                x -= 1
            else:
                break
                
        return a == 1