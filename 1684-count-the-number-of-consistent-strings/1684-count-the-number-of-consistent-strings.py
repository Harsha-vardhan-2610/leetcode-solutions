class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                c += 1
        return c