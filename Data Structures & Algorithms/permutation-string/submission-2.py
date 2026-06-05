class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        if matches == 26:
            return True

        for r in range(len(s1), len(s2)):
            l = r - len(s1)

            # removed s2[l], added s2[r]
            # update counter arrays and matches accordingly
            leftIdx = ord(s2[l]) - ord('a')
            s2Count[leftIdx] -= 1
            if s2Count[leftIdx] == s1Count[leftIdx]:
                matches += 1
            elif s2Count[leftIdx] + 1 == s1Count[leftIdx]:
                matches -= 1

            rightIdx = ord(s2[r]) - ord('a')
            s2Count[rightIdx] += 1
            if s2Count[rightIdx] == s1Count[rightIdx]:
                matches += 1
            elif s2Count[rightIdx] - 1 == s1Count[rightIdx]:
                matches -= 1

            if matches == 26:
                return True    
        
        return False