class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestSeen = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = largestSeen
            largestSeen = max(largestSeen, curr)
        return arr