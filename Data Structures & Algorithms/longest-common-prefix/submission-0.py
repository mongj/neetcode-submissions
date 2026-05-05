class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for s in strs[1:]:
            # compare lcp and s, then update lcp
            tmp = ""
            for i in range(min(len(s), len(lcp))):
                if lcp[i] == s[i]:
                    tmp += lcp[i]
                else:
                    break
            lcp = tmp
        return lcp