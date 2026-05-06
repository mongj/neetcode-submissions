class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums) - 1):
            prefix[i] = nums[i] * prefix[i - 1]
            rev_i = len(nums) - i - 1
            suffix[rev_i] = nums[rev_i] * suffix[(rev_i + 1) % len(nums)]
        
        out = [1] * len(nums)
        for i in range(len(nums)):
            out[i] = prefix[i - 1] * suffix[(i + 1) % len(nums)]
        
        return out