class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        l = 0
        while l < len(s2):
            if s2[l] not in freq:
                l += 1
                continue
            
            r = l
            remainingFreq = freq.copy()
            while r < len(s2):
                if s2[r] in remainingFreq:
                    if remainingFreq[s2[r]] == 1:
                        remainingFreq.pop(s2[r])
                    else:
                        remainingFreq[s2[r]] -= 1
                    r += 1
                else:
                    break
                if len(remainingFreq) == 0:
                    return True
            l += 1
        
        return False