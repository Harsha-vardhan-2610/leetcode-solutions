class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    c += abs(i - j)
                    break
        return c