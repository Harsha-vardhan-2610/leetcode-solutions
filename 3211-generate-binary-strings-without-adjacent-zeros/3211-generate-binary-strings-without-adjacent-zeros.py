class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        valid = ["0", "1"]

        for _ in range(n - 1):
            l = []
            for s in valid:
                if s[-1] == '1':
                    l.append(s + '0')
                    l.append(s + '1')
                else:
                    l.append(s + '1')
                valid = l
        return valid