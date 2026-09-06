class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        working_set = []

        nums.sort()

        def dfs(n: int) -> None:
            if n >= len(nums):
                subsets.append(working_set.copy())
                return
            
            working_set.append(nums[n])
            dfs(n+1)

            working_set.pop()
            # after excluding nums[n], we skip all the subsequent elements
            # with the same value as nums[n]
            while n + 1 < len(nums) and nums[n] == nums[n+1]:
                n += 1
            # recurse on the next distinct element
            dfs(n+1)
        
        dfs(0)

        return subsets