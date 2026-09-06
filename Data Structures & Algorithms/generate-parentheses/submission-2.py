class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        working_set = []
        open_count = 0
        close_count = 0

        def dfs(i: int) -> None:
            nonlocal open_count
            nonlocal close_count

            if i == 2 * n:
                res.append("".join(working_set))
                return
            
            # case 1: add ( if valid
            if open_count < n:
                working_set.append('(')
                open_count += 1
                dfs(i+1)

                # revert the state
                working_set.pop()
                open_count -= 1

            # case 2: add ) if valid
            if i > 0 and close_count < n and close_count < open_count:
                working_set.append(')')
                close_count += 1
                dfs(i+1)
            
                # revert the state
                working_set.pop()
                close_count -= 1
            
        dfs(0)

        return res