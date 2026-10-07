class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = 0
        for n in hours:
            if n >= target:
                c += 1
        return c