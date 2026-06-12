class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        buf = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                buf.append(nums[l]*nums[l])
                l += 1
            else:
                buf.append(nums[r]*nums[r])
                r -= 1
        return buf[::-1]