class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if (s[i] in sMap and sMap[s[i]] != t[i]) or (t[i] in tMap and tMap[t[i]] != s[i]):
                return False
            else:
                sMap[s[i]] = t[i]
                tMap[t[i]] = s[i]
        return True