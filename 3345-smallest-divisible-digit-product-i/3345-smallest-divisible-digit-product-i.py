class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def pro(n):
            f = 1
            while n > 0:
                f *= (n % 10)
                n //= 10
            return f

        for i in range(n, 101):
            if pro(i) % t == 0:
                return i