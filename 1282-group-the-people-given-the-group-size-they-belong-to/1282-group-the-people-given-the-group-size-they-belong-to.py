class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        l = []
        n = len(groupSizes)
        for i in range(n):
            l.append([groupSizes[i], i])
        m = sorted(l, key = lambda x : x[0])
        h = []
        i = 0
        while i < n:
            k = m[i][0]
            group = []
            for j in range(i, i + k):
                group.append(m[j][1])
            h.append(group)
            i += k
        return h