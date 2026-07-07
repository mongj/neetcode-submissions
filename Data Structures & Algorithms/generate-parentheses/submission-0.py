class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s: str) -> bool:
            pList = list(s)
            if pList.count('(') > n or pList.count(')') > n:
                return False
            stack = []
            for p in pList:
                if p == '(':
                    stack.append(p)
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return True

        state = ['(']

        while len(state[0]) < (2 * n):
            newState = []
            for s in state:
                for b in ['(', ')']:
                    newStr = s + b
                    if isValid(newStr):
                        newState.append(newStr)
                state = newState

        return state


        # def isValid(s: str) -> bool:
        #     return True

        # def dfs():
        #     if isValid():
        #         #
        #     else:
        #         return
            
        #     for b in ['(', ')']:
        #         out = [s + b for s in out]
        #         dfs()
        #         out = [s[:-1] for s in out]

        # dfs()

        return out