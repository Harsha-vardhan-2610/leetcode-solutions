from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = 'aeiou'
        a = ''
        b = ''
        for i in s:
            if i in v:
                a += i
            else:
                b += i
        x = Counter(a)
        y = Counter(b)

        return max(x.values(), default = 0) + max(y.values(), default = 0)