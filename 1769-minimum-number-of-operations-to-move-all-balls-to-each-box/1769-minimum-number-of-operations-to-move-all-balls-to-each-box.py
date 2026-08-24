class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        cost = 0
        right = 0
        for i in range(n):
            if boxes[i] == '1':
                cost += i
                right += 1
        left = 0       
        for i in range(n):
            ans[i] = cost
            if boxes[i] == '1':
                left += 1
                right -= 1
            cost += left - right
        return ans