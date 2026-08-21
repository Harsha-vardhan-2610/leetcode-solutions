class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s = ""
        for word in words:
            c = 0
            for ch in word:
                c += weights[ord(ch) - ord('a')]
            c %= 26
            s += chr(ord('z') - c)
        return s