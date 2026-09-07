class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        c, x = 0, k

        for num in nums:
            if num > x:
                break

            x += 1
            c += num
    
        return ((x * (x + 1)) // 2) - c