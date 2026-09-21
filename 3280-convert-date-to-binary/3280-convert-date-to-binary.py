class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s = date.split("-")
        d = list(map(lambda x : bin(int(x))[2:], s))
        return "-".join(d)