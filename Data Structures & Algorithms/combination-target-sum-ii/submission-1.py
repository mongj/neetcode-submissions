class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        working_set = []

        def dfs(i: int, target: int) -> None:
            if target == 0:
                res.append(working_set.copy())
                return
            if i >= len(candidates) or target < 0:
                return

            # case 1: use the number
            working_set.append(candidates[i])
            dfs(i+1, target - candidates[i])

            # case 2: don't use the number
            # in this case, we'll recurse from the next distinct number
            working_set.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, target)
        
        candidates.sort()
        dfs(0, target)

        return res