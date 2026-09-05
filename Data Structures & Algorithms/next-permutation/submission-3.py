class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            # i is the first element we've seen thats smaller than the next
            # so we want to swap it with the second smallest element
            nextSmallestIndex = i+1
            for j in range(i+1, n):
                if nums[j] > nums[i] and nums[j] < nums[nextSmallestIndex]:
                    nextSmallestIndex = j
            # swap nums[i] and nums[nextSmallestIndex]
            nums[i], nums[nextSmallestIndex] = nums[nextSmallestIndex], nums[i]
        
        # reverse nums[i+1..n-1]
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1