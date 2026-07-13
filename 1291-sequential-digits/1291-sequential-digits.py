class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def generate():
            q = [*range(1, 10)]
            for x in q:
                d = x % 10
                if d < 9:
                    q.append(x * 10 + d + 1)
            return q
        nums = generate()
        return [x for x in nums if low <= x <= high]