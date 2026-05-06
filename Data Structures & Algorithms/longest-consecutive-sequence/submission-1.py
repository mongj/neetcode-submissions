class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeqLen = 0
        s = set(nums)
        while len(s) > 0:
            n = s.pop()
            currSeqLen = 1
            nextn = n + 1
            while nextn in s:
                s.remove(nextn)
                currSeqLen += 1
                nextn += 1
            nextn = n - 1
            while nextn in s:
                s.remove(nextn)
                currSeqLen += 1
                nextn -= 1
            longestSeqLen = max(longestSeqLen, currSeqLen)
        return longestSeqLen