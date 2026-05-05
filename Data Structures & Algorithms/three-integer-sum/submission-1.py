class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums.sort()
        n = len(nums)
        print(nums)
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = n - 1
                while k > j and nums[i] + nums[j] + nums[k] >= 0:
                    if nums[i] + nums[j] + nums[k] == 0:
                        out.add((nums[i], nums[j], nums[k]))
                        break
                    k -= 1

        return [list(i) for i in out]