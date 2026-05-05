class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            # store partial product in output array
            output[i] = output[i + 1] * nums[i + 1]
        running_product = nums[0]
        for i in range(1, len(nums)):
            output[i] = output[i] * running_product
            running_product *= nums[i]
        return output

# 1 a a a
# b 1 b b
# c c 1 c
# d d d 1