class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = list(word)
        d = 0
        for i in range(len(l)):
            if l[i] == ch:
                d = i
                break
        x = l[d::-1]
        y = l[d+1::]
        return "".join(x + y)