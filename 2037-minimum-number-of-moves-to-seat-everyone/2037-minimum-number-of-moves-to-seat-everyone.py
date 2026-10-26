class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        s = sorted(seats)
        st = sorted(students)
        c = 0
        for i in range(len(s)):
            c += abs(s[i] - st[i])
        return c