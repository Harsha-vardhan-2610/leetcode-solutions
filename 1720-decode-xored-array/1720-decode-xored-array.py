class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = []
        l.append(first)
        i = 0
        while i < len(encoded):
            l.append(first ^ encoded[i])
            first = l[i+1]
            i += 1
        
        return l