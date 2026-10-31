class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l = []
        for i in range(len(bank)):
            if bank[i].count('1') != 0:
                l.append(bank[i].count('1'))
        
        if len(l) < 2:
            return 0
        else:
            c = 0
            for i in range(len(l) - 1):
                c += l[i] * l[i + 1]
            return c