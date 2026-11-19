class Solution:
    def minimumSum(self, num: int) -> int:
        s = list(str(num))
        c = sorted(s)
        return (int(c[0]) + int(c[1])) * 10 + (int(c[2]) + int(c[3]))