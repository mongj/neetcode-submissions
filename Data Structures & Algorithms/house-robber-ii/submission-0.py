class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def sub(i: int, j: int) -> int:
            if i > j:
                return 0
            
            maxl, maxr = 0, 0
            while i <= j:
                maxl, maxr = maxr, max(maxr, maxl + nums[i])
                i += 1
            return maxr

        return max(sub(2, n-2) + nums[0],
                   sub(1, n-1))