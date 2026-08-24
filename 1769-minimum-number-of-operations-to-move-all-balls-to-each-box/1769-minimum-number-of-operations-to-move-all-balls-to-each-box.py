class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        a = []
        for i in range(len(boxes)):
            c = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    c += abs(i - j)
                if j == len(boxes) - 1:
                    a.append(c)
        return a