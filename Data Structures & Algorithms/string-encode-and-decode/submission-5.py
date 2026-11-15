class Solution:
    SEPARATOR = "."

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            out.extend([str(len(s)), self.SEPARATOR, s])
        return "".join(out)
        
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            currSegmentLenStr = ""
            while s[i] != self.SEPARATOR:
                currSegmentLenStr += s[i]
                i += 1
            s_start = i + 1
            s_end = s_start + int(currSegmentLenStr)
            out.append(s[s_start:s_end])
            i = s_end

        return out