class Solution:
    def maxProduct(self, n: int) -> int:
        arr = sorted(list(str(n)))
        return int(arr[-1]) * int(arr[-2])