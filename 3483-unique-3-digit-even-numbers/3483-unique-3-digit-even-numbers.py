class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c = Counter(digits)

        res = 0
        for n in range(100, 1000, 2):
            i, r = divmod(n, 100)
            j, k = divmod(r, 10)
            res += c[i] > 0 and c[j] > (i == j) and c[k] > (i == k) + (j == k)
        
        return res