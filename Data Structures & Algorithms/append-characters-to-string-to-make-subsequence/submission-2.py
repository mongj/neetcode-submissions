class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si = ti = 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                si += 1
        
        return len(t) - ti