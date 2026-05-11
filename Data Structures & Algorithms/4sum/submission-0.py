class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = {}
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                complement = target - nums[i] - nums[j]
                l = j + 1
                r = n - 1
                while l < r:
                    if nums[l] + nums[r] == complement:
                        arr = [nums[i], nums[j], nums[l], nums[r]]
                        res["".join(map(str, arr))] = arr
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > complement:
                        r -= 1
                    else:
                        l += 1
        return list(res.values())