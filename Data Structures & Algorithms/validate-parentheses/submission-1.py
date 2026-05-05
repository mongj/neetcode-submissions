class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                seen.append(c)
            elif len(seen) == 0:
                return False
            else:
                last_item = seen.pop()
                if c == "]" and last_item != "[":
                    return False
                if c == ")" and last_item != "(":
                    return False
                if c == "}" and last_item != "{":
                    return False
        return len(seen) == 0
                