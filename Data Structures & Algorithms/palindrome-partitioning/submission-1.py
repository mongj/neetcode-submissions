class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        working_set = []

        def isPalindrome(ss: str) -> bool:
            l, r = 0, len(ss) - 1
            while l < r:
                if ss[l] != ss[r]:
                    return False
                l += 1
                r -= 1
            return True

        # i is the index of the first character in the next substring
        # j is the current pointer
        def dfs(i: int, j: int) -> None:
            if j > len(s):
                return

            # print(f"i: {i} j: {j}")
            # print(f"  {working_set}")
            # check if current state is valid
            for substring in working_set:
                if not isPalindrome(substring):
                    # print("  working_set is invalid, returning")
                    return

            if i == len(s):
                res.append(working_set.copy())
                # print("  working_set is valid and complete!")
                return

            # case 1: partition after the ith element
            working_set.append(s[i:j+1])
            # print(f"  going to {j+1}, {j+1}")
            dfs(j+1, j+1)

            # case 2: do not partition
            working_set.pop()
            # print(f"  going to {i}, {j+1}")
            dfs(i, j+1)
            
        
        dfs(0, 0)

        return res