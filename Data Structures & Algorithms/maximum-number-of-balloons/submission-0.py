class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = { "b": 1, "a": 1, "l": 2, "o": 2, "n": 1 }
        have = { "b": 0, "a": 0, "l": 0, "o": 0, "n": 0 }
        for c in text:
            if c in have:
                have[c] += 1
        
        return min([a // b for a, b in zip(list(have.values()), list(need.values()))])
