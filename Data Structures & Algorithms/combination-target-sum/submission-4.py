class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        working_set = []

        def dfs(i: int, target: int) -> None:
            if i >= len(nums) or target < 0:
                return
            if target == 0:
                res.append(working_set.copy())
                return
            
            # case 1: use the num
            working_set.append(nums[i])
            dfs(i, target - nums[i])

            # case 2: dont use the num
            working_set.pop()
            dfs(i + 1, target)
        
        dfs(0, target)

        return res

        # if not nums or target < 0:
        #     return []
        # if target == 0:
        #     return [[]]

        # # case 1: use nums[0]
        # sub1 = [[nums[0]] + s for s in self.combinationSum(nums, target - nums[0])]
        # # case 2: don't use nums[0]
        # sub2 = self.combinationSum(nums[1:], target)

        # return sub1 + sub2
