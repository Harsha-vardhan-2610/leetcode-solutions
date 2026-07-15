class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(o, e):
            if e == 0:
                return o
            return gcd(e, o % e)
        o = n * n
        e = n * (n + 1)
        return gcd(o, e)