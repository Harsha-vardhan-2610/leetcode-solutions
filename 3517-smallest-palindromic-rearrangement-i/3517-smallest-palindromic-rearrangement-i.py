class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        l = n // 2
        ns = sorted(s[:l])
        x = "".join(ns)
        return x + x[::-1] if n % 2 == 0 else x + s[l] + x[::-1]