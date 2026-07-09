class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l = []
        s = set()
        i = 0
        c = 0
        while i < len(A) and i < len(B):
            if A[i] not in s:
                s.add(A[i])
            else:
                c += 1
            if B[i] not in s:
                s.add(B[i])
            else:
                c += 1
            l.append(c)
            i += 1
        return l