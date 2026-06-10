class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        maxOddFreq = max([f for f in freq if f % 2 == 1])
        minEvenFreq = min([f for f in freq if f % 2 == 0 and f != 0])

        return maxOddFreq - minEvenFreq