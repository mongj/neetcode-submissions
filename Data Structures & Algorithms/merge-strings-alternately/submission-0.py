class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        wl1 = len(word1)
        wl2 = len(word2)
        for i in range(min(wl1, wl2)):
            s += word1[i] + word2[i]
        if wl1 < wl2:
            s += word2[wl1:wl2]
        else:
            s += word1[wl2:wl1]
        return s