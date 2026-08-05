class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stMap = {}
        tsMap = {}
        for i in range(len(s)):
            if s[i] in stMap and stMap[s[i]] != t[i]:
                return False
            if t[i] in tsMap and tsMap[t[i]] != s[i]:
                return False
            
            stMap[s[i]] = t[i]
            tsMap[t[i]] = s[i]
        return True
