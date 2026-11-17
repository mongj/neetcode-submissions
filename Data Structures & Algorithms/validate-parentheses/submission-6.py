class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0