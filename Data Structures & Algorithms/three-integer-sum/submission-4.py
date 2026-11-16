class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []
        i = 0
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                elif curr > 0:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
            while i < n - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return out
        