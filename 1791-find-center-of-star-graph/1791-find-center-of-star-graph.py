class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        a = edges[0][0]
        b = edges[0][1]
        c = edges[1][0]
        d = edges[1][1]
        return a if a == b or a == c or a == d else b if b == c or b == d else c