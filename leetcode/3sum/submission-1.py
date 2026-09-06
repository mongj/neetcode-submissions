class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        matches = set()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    matches.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif curr > 0:
                    k -= 1
                else:
                    j += 1
        return [list(tpl) for tpl in matches]