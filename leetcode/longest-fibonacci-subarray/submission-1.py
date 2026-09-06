class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Subarray of length 2 is always Fibonacci.
        start, end = 0, 1
        longestSeen = 2
        i = end + 1
        while i < len(nums):
            # check if the number at index i can be appended to the fib subarray
            if nums[i] != nums[i - 1] + nums[i - 2]:
                longestSeen = max(longestSeen, end - start + 1)
                start = i - 1
            end = i
            i += 1
        return max(longestSeen, end - start + 1)