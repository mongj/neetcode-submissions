import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        working_set = []

        def dfs(n: int) -> None:
            if n >= len(nums):
                res.append(working_set.copy())
                return
            
            working_set.append(nums[n])
            dfs(n+1)

            working_set.pop()
            dfs(n+1)
        
        dfs(0)

        return res