class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentMajorityElement = nums[0]
        leadScore = 1
        for num in nums[1:]:
            if num == currentMajorityElement:
                leadScore += 1
            elif leadScore > 0:
                leadScore -= 1
            else:
                # if leadScore is 0, we swap the majority element
                currentMajorityElement = num
                leadScore += 1
        return currentMajorityElement