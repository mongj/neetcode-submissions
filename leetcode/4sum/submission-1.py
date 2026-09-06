class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        matches = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l, r = j + 1, n - 1
                while l < r:
                    currSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if currSum == target:
                        matches.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif currSum > target:
                        r -= 1
                    else:
                        l += 1
        return [list(tpl) for tpl in matches]