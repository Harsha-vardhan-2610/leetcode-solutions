class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, m, n = [], [], []
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i == pivot:
                m.append(i)
            else:
                n.append(i)

        return l + m + n