class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []
        for word in words:
            for target in words:
                if word != target and word in target:
                    matches.append(word)
                    break
        return matches