class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def sumpro(n):
            c, f = 0, 1
            while n > 0:
                c += n % 10
                f *= n % 10
                n //= 10
            return c + f
        return n % sumpro(n) == 0