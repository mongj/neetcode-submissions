class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []
        working_set = []

        if len(digits) == 0:
            return res

        def dfs(n: int) -> None:
            if n == len(digits):
                res.append("".join(working_set))
                return

            for letter in digitMap[digits[n]]:
                working_set.append(letter)
                dfs(n+1)
                working_set.pop()
        
        dfs(0)
        
        return res