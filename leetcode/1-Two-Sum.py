class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumToIndex = {}
        n = len(nums)
        for i in range(n):
            wantNum = target - nums[i]
            if wantNum in seenNumToIndex:
                return [seenNumToIndex[wantNum], i]
            seenNumToIndex[nums[i]] = i
