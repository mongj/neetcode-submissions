class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "-" + s
        return out
        
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            count = ""
            while s[i].isdigit():
                count += s[i]
                i += 1
            i += 1
            out.append(s[i:i + int(count)])
            i = i + int(count)
        return out