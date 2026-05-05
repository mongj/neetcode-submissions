class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            k = "-".join(map(str, counter))
            if k in h:
                h[k].append(s)
            else:
                h[k] = [s]
        return list(h.values())
