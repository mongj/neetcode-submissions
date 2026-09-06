class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        working_set = []
        used = [False] * n

        def dfs(i: int) -> None:
            if i == n:
                res.append(working_set.copy())
                return
            
            # at each level, we iterate through nums and pick 1 number to use
            for j in range(n):
                if not used[j]:
                    used[j] = True
                    working_set.append(nums[j])
                    dfs(i+1)

                    # free up nums[j]
                    working_set.pop()
                    used[j] = False

        dfs(0)

        return res