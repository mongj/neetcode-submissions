class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        # sub(i) returns length of LIS using index i
        def sub(i: int, cap: int) -> int:
            if (i, cap) in cache:
                return cache[(i, cap)]
            
            if i == 0:
                return 1

            # case 1: use i, then find the next smallest element
            if nums[i] < cap:
                j = i
                while j >= 0 and nums[j] >= nums[i]:
                    j -= 1
                s1 = 1 + sub(j, nums[i]) if j >= 0 else 1
            else:
                s1 = 0
            
            # case 2: skip i
            s2 = sub(i - 1, cap)

            cache[(i, cap)] = max(s1, s2)
            return cache[(i, cap)]
        
        ans = sub(len(nums) - 1, max(nums) + 1)
        return ans