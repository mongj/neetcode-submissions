class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        # if current pair == target, return
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            # else if current pair > target, decrement r
            elif numbers[l] + numbers[r] > target:
                r -= 1
            # else increment l
            else:
                l += 1
        return [0, 0] # should never reach here
        
