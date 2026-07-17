class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)

        for a in nums:
            freq[a] += 1
        
        hcf = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            hcf[i] = sm * (sm - 1) // 2 - sum(hcf[i::i])
        
        hcf = list(accumulate(hcf))

        return [bisect.bisect_right(hcf, q) for q in queries]