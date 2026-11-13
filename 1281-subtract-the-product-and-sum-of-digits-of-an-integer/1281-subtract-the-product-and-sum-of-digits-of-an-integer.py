class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        c, d = 0, 1
        while n != 0:
            c += n % 10
            d *= n % 10
            n //= 10
        return d - c