from collections import Counter
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        c = Counter(str(n))
        res = 0

        for x, y in c.items():
            res += int(x) * y
        
        return res