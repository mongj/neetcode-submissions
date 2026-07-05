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

        if len(digits) == 0:
            return []

        lastDigit = digits[-1]
        sub = self.letterCombinations(digits[:-1])
        if sub:
            return [s + c for s in sub for c in digitMap[lastDigit]]
        else:
            return digitMap[lastDigit]
