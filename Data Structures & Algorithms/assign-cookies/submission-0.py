class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        contentCount = 0
        while i < len(g) and j < len(s):
            while j < len(s) and s[j] < g[i]:
                j += 1

            if j == len(s):
                break

            contentCount += 1
            i += 1
            j += 1
            
        return contentCount