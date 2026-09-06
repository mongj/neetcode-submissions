class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = {}
        working_set = []

        nums.sort()

        def dfs(n: int) -> None:
            if n >= len(nums):
                key = "".join([str(a) for a in working_set])
                if key not in subsets:
                    subsets[key] = working_set.copy()
                return
            
            working_set.append(nums[n])
            dfs(n+1)

            working_set.pop()
            dfs(n+1)
        
        dfs(0)

        return list(subsets.values())