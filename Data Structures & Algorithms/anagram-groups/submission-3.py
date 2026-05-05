from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[self.hashString(s)].append(s)
        return list(d.values())
    
    def hashString(self, s: str) -> str:
        tmp = [0]*26
        for c in s:
            tmp[ord(c) - 97] += 1
        s = ""
        for i in range(26):
            s += chr(i + 97)
            s += str(tmp[i])
        return s