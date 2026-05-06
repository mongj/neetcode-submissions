class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    s.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return [list(n) for n in s]